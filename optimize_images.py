#!/usr/bin/env python3
"""
Image optimization script for Muse Bar website
Resizes and optimizes images to reduce file size for web deployment
"""

from PIL import Image
import os
import sys

# Maximum dimensions for web images
MAX_WIDTH = 1920
MAX_HEIGHT = 1920
QUALITY = 85  # JPEG quality (0-100)

def optimize_image(input_path, output_path=None, max_width=MAX_WIDTH, max_height=MAX_HEIGHT):
    """Optimize an image by resizing and compressing"""
    if output_path is None:
        output_path = input_path
    
    try:
        # Open image
        img = Image.open(input_path)
        original_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
        
        # Get original dimensions
        width, height = img.size
        print(f"Processing: {input_path}")
        print(f"  Original: {width}x{height}, {original_size:.2f}MB")
        
        # Calculate new dimensions maintaining aspect ratio
        if width > max_width or height > max_height:
            ratio = min(max_width / width, max_height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            print(f"  Resized to: {new_width}x{new_height}")
        
        # Convert RGBA to RGB if needed (for JPEG)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Create white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        
        # Determine output format
        ext = os.path.splitext(output_path)[1].lower()
        
        # Save optimized image
        if ext in ('.jpg', '.jpeg'):
            img.save(output_path, 'JPEG', quality=QUALITY, optimize=True)
        elif ext == '.png':
            # For PNG, try to optimize
            img.save(output_path, 'PNG', optimize=True)
        else:
            img.save(output_path, optimize=True)
        
        new_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
        reduction = ((original_size - new_size) / original_size) * 100
        print(f"  Optimized: {new_size:.2f}MB (reduced by {reduction:.1f}%)")
        print()
        
        return True
        
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False

def main():
    """Optimize all large images"""
    images_to_optimize = [
        'images/cavepv.png',
        'images/carrousel/cave.png',
        'images/carrousel/bar.jpg',
        'images/carrousel/planche.jpg',
        'images/carrousel/biere.jpg',
        'images/homepage.png',
        'images/dehors.png',
        'images/carrousel/terrasse.png',
    ]
    
    print("=" * 60)
    print("Image Optimization Script")
    print("=" * 60)
    print()
    
    # Create backup directory
    backup_dir = 'images_backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Created backup directory: {backup_dir}")
    
    optimized_count = 0
    for img_path in images_to_optimize:
        if os.path.exists(img_path):
            # Backup original
            backup_path = os.path.join(backup_dir, os.path.basename(img_path))
            if not os.path.exists(backup_path):
                import shutil
                shutil.copy2(img_path, backup_path)
                print(f"Backed up: {img_path} -> {backup_path}")
            
            # Optimize
            if optimize_image(img_path):
                optimized_count += 1
        else:
            print(f"Warning: {img_path} not found, skipping...")
    
    print("=" * 60)
    print(f"Optimization complete! Processed {optimized_count} images.")
    print(f"Original images backed up in: {backup_dir}/")
    print("=" * 60)

if __name__ == '__main__':
    main()

