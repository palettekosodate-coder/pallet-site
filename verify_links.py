#!/usr/bin/env python3
"""
Verify all internal links in the palette-site.
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse

SITE_ROOT = "/sessions/blissful-zealous-volta/mnt/hp-pallet/palette-site"

def is_external_url(href):
    """Check if URL is external or should be skipped."""
    if not href:
        return True
    
    # Skip external protocols
    if href.startswith(('http://', 'https://', 'mailto:', 'javascript:', 'tel:')):
        return True
    
    # Skip anchors (but check if they're valid)
    if href.startswith('#'):
        return True
    
    return False

def resolve_path(file_path, href):
    """Resolve a relative path from a file's directory."""
    file_dir = os.path.dirname(file_path)
    
    # Remove any trailing anchors
    href_without_anchor = href.split('#')[0]
    
    if not href_without_anchor:
        return None
    
    # Resolve relative to file's directory
    resolved = os.path.normpath(os.path.join(file_dir, href_without_anchor))
    return resolved

def find_hrefs_and_srcs(html_content, file_path):
    """Extract all href and src attributes from HTML content."""
    links = []
    
    # Find all href="..." attributes
    href_pattern = r'href=(["\'])([^"\']*)\1'
    for match in re.finditer(href_pattern, html_content):
        href = match.group(2)
        line_num = html_content[:match.start()].count('\n') + 1
        links.append(('href', href, line_num))
    
    # Find all src="..." attributes
    src_pattern = r'src=(["\'])([^"\']*)\1'
    for match in re.finditer(src_pattern, html_content):
        src = match.group(2)
        line_num = html_content[:match.start()].count('\n') + 1
        links.append(('src', src, line_num))
    
    return links

def check_old_style_references(html_content, file_path):
    """Check for old-style path references."""
    issues = []
    
    # Check for palette-logo.png without images/ prefix (in root files only)
    if '/events/' not in file_path:
        if re.search(r'palette-logo\.png', html_content):
            lines = html_content.split('\n')
            for i, line in enumerate(lines, 1):
                if 'palette-logo.png' in line:
                    issues.append({
                        'file': file_path,
                        'line': i,
                        'type': 'old-style-path',
                        'message': f'Found palette-logo.png without images/ prefix'
                    })
    
    # Check for palette hero.mp4 (with space instead of hyphen)
    if re.search(r'palette\s+hero\.mp4', html_content):
        lines = html_content.split('\n')
        for i, line in enumerate(lines, 1):
            if 'palette' in line and 'hero.mp4' in line and ' hero' in line:
                issues.append({
                    'file': file_path,
                    'line': i,
                    'type': 'old-style-path',
                    'message': f'Found "palette hero.mp4" (should be palette-hero.mp4 with hyphen)'
                })
    
    # Check for event-*.html style old names in root files
    if '/events/' not in file_path:
        old_event_pattern = r'event-\w+-\d+\.html'
        if re.search(old_event_pattern, html_content):
            lines = html_content.split('\n')
            for i, line in enumerate(lines, 1):
                if re.search(old_event_pattern, line):
                    issues.append({
                        'file': file_path,
                        'line': i,
                        'type': 'old-style-path',
                        'message': f'Found old-style event reference (should use events/ subfolder or ../)'
                    })
    
    return issues

def main():
    """Main function to verify all links."""
    
    site_root = Path(SITE_ROOT)
    
    if not site_root.exists():
        print(f"Error: Site root does not exist: {SITE_ROOT}")
        return
    
    # Find all HTML files
    html_files = list(site_root.glob("*.html")) + list(site_root.glob("events/*.html"))
    html_files.sort()
    
    total_links = 0
    broken_links = []
    old_style_refs = []
    
    print(f"Verifying links in {len(html_files)} HTML files...\n")
    
    for html_file in html_files:
        file_path = str(html_file)
        rel_path = os.path.relpath(file_path, SITE_ROOT)
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")
            continue
        
        # Check for old-style references
        old_refs = check_old_style_references(content, file_path)
        old_style_refs.extend(old_refs)
        
        # Find all links
        links = find_hrefs_and_srcs(content, file_path)
        
        for attr_type, link, line_num in links:
            total_links += 1
            
            # Skip external URLs
            if is_external_url(link):
                continue
            
            # Remove anchors for checking file existence
            link_without_anchor = link.split('#')[0]
            
            if not link_without_anchor:
                continue
            
            # Resolve the path
            resolved = resolve_path(file_path, link)
            
            if not resolved:
                continue
            
            # Check if file exists
            if not os.path.exists(resolved):
                broken_links.append({
                    'file': rel_path,
                    'line': line_num,
                    'attribute': attr_type,
                    'link': link,
                    'resolved_path': os.path.relpath(resolved, SITE_ROOT)
                })
    
    # Print summary
    print("=" * 80)
    print("LINK VERIFICATION SUMMARY")
    print("=" * 80)
    print(f"Total links checked: {total_links}")
    print(f"Broken links found: {len(broken_links)}")
    print(f"Old-style references found: {len(old_style_refs)}")
    print()
    
    if broken_links:
        print("BROKEN LINKS:")
        print("-" * 80)
        for item in broken_links:
            print(f"File: {item['file']}:{item['line']}")
            print(f"  Attribute: {item['attribute']}")
            print(f"  Link: {item['link']}")
            print(f"  Resolved to: {item['resolved_path']}")
            print()
    
    if old_style_refs:
        print("OLD-STYLE REFERENCES:")
        print("-" * 80)
        for item in old_style_refs:
            print(f"File: {item['file']}:{item['line']}")
            print(f"  Issue: {item['message']}")
            print()
    
    if not broken_links and not old_style_refs:
        print("All links are valid and no old-style references found!")
        print()

if __name__ == "__main__":
    main()
