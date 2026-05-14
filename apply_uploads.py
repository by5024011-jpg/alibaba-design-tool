#!/usr/bin/env python3
"""Fix real file upload + mobile responsive."""

FILE = 'index.html'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = 0

# === UPLOAD ZONE REPLACEMENTS ===

# 1. Single image upload
old = '''case 'image':
      h += `<div class="upload-zone" onclick="simulateUpload(this,'image')" id="${fid}">
        <div class="upload-zone-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg></div>
        <div class="upload-zone-text">点击上传 ${inp.label}</div>
        <div class="upload-zone-meta">${inp.hint||'支持 JPG / PNG / SVG'}</div>
        <div class="upload-preview-grid" style="display:none;"></div>
      </div>`;'''
new = '''case 'image':
      h += `<div class="upload-zone" id="${fid}" data-upload-type="image">
        <input type="file" hidden accept="image/*" onchange="handleFileSelect(this,'image')">
        <div class="upload-zone-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg></div>
        <div class="upload-zone-text">点击或拖拽上传 ${inp.label}</div>
        <div class="upload-zone-meta">${inp.hint||'支持 JPG / PNG / SVG'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
if old in content:
    content = content.replace(old, new)
    replacements += 1
    print('OK: image upload')
else:
    print('MISS: image upload')

# 2. Multiple images upload
old = '''case 'images':
      h += `<div class="upload-zone" onclick="simulateUpload(this,'images')" id="${fid}">
        <div class="upload-zone-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
        <div class="upload-zone-text">点击上传 ${inp.label}</div>
        <div class="upload-zone-meta">${inp.hint||'支持批量上传' + (inp.max ? '，最多'+inp.max+'张' : '')}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
new = '''case 'images':
      h += `<div class="upload-zone" id="${fid}" data-upload-type="images">
        <input type="file" hidden accept="image/*" multiple onchange="handleFileSelect(this,'images')">
        <div class="upload-zone-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
        <div class="upload-zone-text">点击或拖拽上传 ${inp.label}</div>
        <div class="upload-zone-meta">${inp.hint||'支持批量上传' + (inp.max ? '，最多'+inp.max+'张' : '')}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
if old in content:
    content = content.replace(old, new)
    replacements += 1
    print('OK: images upload')
else:
    print('MISS: images upload')

# 3. Video upload
old = '''case 'video':
      h += `<div class="video-upload-zone" onclick="simulateUpload(this,'video')" id="${fid}">
        <div class="video-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
        <div class="upload-zone-text">点击上传视频</div>
        <div class="upload-zone-meta">${inp.hint||'建议 MP4 格式，<=60s'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
new = '''case 'video':
      h += `<div class="video-upload-zone" id="${fid}" data-upload-type="video">
        <input type="file" hidden accept="video/*" onchange="handleFileSelect(this,'video')">
        <div class="video-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
        <div class="upload-zone-text">点击或拖拽上传视频</div>
        <div class="upload-zone-meta">${inp.hint||'建议 MP4 格式，<=60s'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
if old in content:
    content = content.replace(old, new)
    replacements += 1
    print('OK: video upload')
else:
    print('MISS: video upload')

# 4. File/folder upload
old = '''case 'file':
    case 'folder':
      h += `<div class="upload-zone" onclick="simulateUpload(this,'folder')" id="${fid}">
        <div class="upload-zone-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
        <div class="upload-zone-text">点击上传${inp.type==='folder'?'文件夹':'文件'}</div>
        <div class="upload-zone-meta">${inp.hint||'支持拖拽文件夹到此处'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
new = '''case 'file':
    case 'folder':
      h += `<div class="upload-zone" id="${fid}" data-upload-type="${inp.type}">
        <input type="file" hidden ${inp.type==='folder'?'webkitdirectory':''} multiple onchange="handleFileSelect(this,'${inp.type}')">
        <div class="upload-zone-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
        <div class="upload-zone-text">点击或拖拽上传${inp.type==='folder'?'文件夹':'文件'}</div>
        <div class="upload-zone-meta">${inp.hint||'支持拖拽' + (inp.type==='folder'?'文件夹':'文件') + '到此处'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
if old in content:
    content = content.replace(old, new)
    replacements += 1
    print('OK: file/folder upload')
else:
    print('MISS: file/folder upload')

# 5. Product card image
old = 'onclick="simulateProductUpload(this)" title="点击上传产品主图"'
new = 'title="点击或拖拽上传产品主图"'
if old in content:
    content = content.replace(old, new)
    replacements += 1
    print('OK: product card title')
else:
    print('MISS: product card title')

old2 = '<div class="product-card-img" id="${cid}_img" title="点击或拖拽上传产品主图">\n            <span class="pc-img-icon"><svg'
new2 = '<div class="product-card-img" id="${cid}_img" title="点击或拖拽上传产品主图">\n            <input type="file" hidden accept="image/*" onchange="handleProductImage(this)">\n            <span class="pc-img-icon"><svg'
if old2 in content:
    content = content.replace(old2, new2)
    replacements += 1
    print('OK: product card file input')
else:
    print('MISS: product card file input')

# 6. Bottom generic upload zone
old = '<div class="upload-zone" onclick="simulateUpload(this)">'
new = '<div class="upload-zone" data-upload-type="generic">\n        <input type="file" hidden multiple onchange="handleFileSelect(this,\\'generic\\')">'
if old in content:
    content = content.replace(old, new)
    replacements += 1
    print('OK: generic upload zone')
else:
    print('MISS: generic upload zone')

print(f'\nTotal upload replacements: {replacements}')
print(f'File: {len(content)} chars')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)
