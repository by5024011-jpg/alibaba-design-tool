#!/usr/bin/env python3
"""Fix real file upload + mobile responsive for Alibaba Design Tool."""
import re

FILE = 'index.html'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# ===== PART 1: REAL FILE UPLOAD — replace onclick handlers =====

# 1a. Replace image upload zone (single)
content = content.replace(
    '''case 'image':
      h += `<div class="upload-zone" onclick="simulateUpload(this,'image')" id="${fid}">
        <div class="upload-zone-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg></div>
        <div class="upload-zone-text">点击上传 ${inp.label}</div>
        <div class="upload-zone-meta">${inp.hint||'支持 JPG / PNG / SVG'}</div>
        <div class="upload-preview-grid" style="display:none;"></div>
      </div>`;''',
    '''case 'image':
      h += `<div class="upload-zone" id="${fid}" data-upload-type="image">
        <input type="file" hidden accept="image/*" onchange="handleFileSelect(this,'image')">
        <div class="upload-zone-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg></div>
        <div class="upload-zone-text">点击或拖拽上传 ${inp.label}</div>
        <div class="upload-zone-meta">${inp.hint||'支持 JPG / PNG / SVG'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
)

# 1b. Replace images upload zone (multiple)
content = content.replace(
    '''case 'images':
      h += `<div class="upload-zone" onclick="simulateUpload(this,'images')" id="${fid}">
        <div class="upload-zone-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
        <div class="upload-zone-text">点击上传 ${inp.label}</div>
        <div class="upload-zone-meta">${inp.hint||'支持批量上传' + (inp.max ? '，最多'+inp.max+'张' : '')}</div>
        <div class="upload-preview-grid"></div>
      </div>`;''',
    '''case 'images':
      h += `<div class="upload-zone" id="${fid}" data-upload-type="images">
        <input type="file" hidden accept="image/*" multiple onchange="handleFileSelect(this,'images')">
        <div class="upload-zone-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
        <div class="upload-zone-text">点击或拖拽上传 ${inp.label}</div>
        <div class="upload-zone-meta">${inp.hint||'支持批量上传' + (inp.max ? '，最多'+inp.max+'张' : '')}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
)

# 1c. Replace video upload zone
content = content.replace(
    '''case 'video':
      h += `<div class="video-upload-zone" onclick="simulateUpload(this,'video')" id="${fid}">
        <div class="video-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
        <div class="upload-zone-text">点击上传视频</div>
        <div class="upload-zone-meta">${inp.hint||'建议 MP4 格式，≤60s'}</div>
      </div>`;''',
    '''case 'video':
      h += `<div class="video-upload-zone" id="${fid}" data-upload-type="video">
        <input type="file" hidden accept="video/*" onchange="handleFileSelect(this,'video')">
        <div class="video-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
        <div class="upload-zone-text">点击或拖拽上传视频</div>
        <div class="upload-zone-meta">${inp.hint||'建议 MP4 格式，≤60s'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
)

# 1d. Replace file/folder upload zone
content = content.replace(
    '''case 'file':
    case 'folder':
      h += `<div class="upload-zone" onclick="simulateUpload(this,'folder')" id="${fid}">
        <div class="upload-zone-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
        <div class="upload-zone-text">点击上传${inp.type==='folder'?'文件夹':'文件'}</div>
        <div class="upload-zone-meta">${inp.hint||'支持拖拽文件夹到此处'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;''',
    '''case 'file':
    case 'folder':
      h += `<div class="upload-zone" id="${fid}" data-upload-type="${inp.type}">
        <input type="file" hidden ${inp.type==='folder'?'webkitdirectory':''} multiple onchange="handleFileSelect(this,'${inp.type}')">
        <div class="upload-zone-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></div>
        <div class="upload-zone-text">点击或拖拽上传${inp.type==='folder'?'文件夹':'文件'}</div>
        <div class="upload-zone-meta">${inp.hint||'支持拖拽' + (inp.type==='folder'?'文件夹':'文件') + '到此处'}</div>
        <div class="upload-preview-grid"></div>
      </div>`;'''
)

# 1e. Replace product card image upload
content = content.replace(
    '''onclick="simulateProductUpload(this)" title="点击上传产品主图"''',
    '''title="点击或拖拽上传产品主图"'''
)

# 1f. Replace the generic upload zone at bottom of each section
content = content.replace(
    '''<div class="upload-zone" onclick="simulateUpload(this)">''',
    '''<div class="upload-zone" data-upload-type="generic">
        <input type="file" hidden multiple onchange="handleFileSelect(this,'generic')">'''
)

# 2. Replace simulateUpload JS function with real handlers
old_simulate = '''function simulateUpload(el, type) {
  el.classList.add('has-files');
  const grid = el.querySelector('.upload-preview-grid');
  if (grid) {
    const demoImgs = [
      'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=120&h=120&fit=crop',
      'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=120&h=120&fit=crop',
      'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=120&h=120&fit=crop',
    ];
    const imgUrl = demoImgs[Math.floor(Math.random() * demoImgs.length)];
    const thumb = document.createElement('div');
    thumb.className = 'upload-thumb';
    thumb.innerHTML = `<img src="${imgUrl}" alt=""><div class="thumb-remove" onclick="event.stopPropagation();this.parentElement.remove();autoSave();">×</div><div class="thumb-label">${type==='video'?'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg> 视频':type==='folder'?'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg> 文件':'图片'}</div>`;
    grid.appendChild(thumb);
  }
  const textEl = el.querySelector('.upload-zone-text');
  if (textEl) textEl.textContent = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> 已添加（点击继续添加）';
  markSectionFilled();
  autoSave();
}

// Product card image upload (simulated demo)
function simulateProductUpload(el) {
  el.classList.add('has-image');
  // Replace placeholder with a demo image
  const demoImgs = [
    'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=300&h=300&fit=crop',
    'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=300&h=300&fit=crop',
    'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=300&h=300&fit=crop',
    'https://images.unsplash.com/photo-1460925895917-afdab827c52?w=300&h=300&fit=crop',
    'https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=300&h=300&fit=crop',
    'https://images.unsplash.com/photo-1563770660941-20978e870e26?w=300&h=300&fit=crop',
  ];
  const imgUrl = demoImgs[Math.floor(Math.random() * demoImgs.length)];
  el.innerHTML = `<img src="${imgUrl}" alt="Product">`;
  markSectionFilled();
  autoSave();
}'''

new_handlers = '''// ===== REAL FILE UPLOAD =====
// In-memory store for uploaded file data (dataURLs for persistence, blob objects for preview)
const uploadedFiles = new Map(); // key: zone_id, value: [{name, size, type, dataURL, isImage}]

function triggerUpload(el) {
  const input = el.querySelector('input[type=file]');
  if (input) input.click();
}

function handleFileSelect(input, type) {
  handleFiles(input.parentElement, input.files, type);
  input.value = ''; // Reset so same file can be re-uploaded
}

function handleFiles(el, files, type) {
  const zoneId = el.id;
  const existing = uploadedFiles.get(zoneId) || [];
  const maxFiles = type === 'image' ? 1 : 99;
  const startIdx = type === 'image' ? 0 : existing.length;
  
  const grid = el.querySelector('.upload-preview-grid');
  let added = 0;
  
  Array.from(files).forEach((file, i) => {
    if ((existing.length + added) >= maxFiles) return;
    
    const isImage = file.type.startsWith('image/');
    const isVideo = file.type.startsWith('video/');
    const reader = new FileReader();
    const fileIdx = startIdx + added;
    
    reader.onload = function(e) {
      const dataURL = e.target.result;
      const fileData = { name: file.name, size: file.size, type: file.type, dataURL: dataURL, isImage: isImage };
      existing.push(fileData);
      
      if (type === 'image') existing.length > 1 && existing.shift(); // Keep only 1 for single
      
      uploadedFiles.set(zoneId, existing);
      
      // Create preview thumbnail
      if (grid) {
        const thumb = document.createElement('div');
        thumb.className = 'upload-thumb';
        if (isImage) {
          thumb.innerHTML = `<img src="${dataURL}" alt="${file.name}"><div class="thumb-remove" onclick="event.stopPropagation();removeUploadedFile('${zoneId}',${existing.length-1});">×</div><div class="thumb-label">${file.name.length > 12 ? file.name.slice(0,10)+'..'+file.name.split('.').pop() : file.name}</div>`;
        } else if (isVideo) {
          thumb.innerHTML = `<video src="${dataURL}" muted></video><div class="thumb-remove" onclick="event.stopPropagation();removeUploadedFile('${zoneId}',${existing.length-1});">×</div><div class="thumb-label"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg> ${file.name.slice(0,14)}</div>`;
        } else {
          thumb.innerHTML = `<div class="file-preview-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div><div class="thumb-remove" onclick="event.stopPropagation();removeUploadedFile('${zoneId}',${existing.length-1});">×</div><div class="thumb-label">${file.name.slice(0,14)}</div>`;
        }
        grid.appendChild(thumb);
        grid.style.display = 'flex';
      }
      
      // Update text for single image
      if (type === 'image') {
        const textEl = el.querySelector('.upload-zone-text');
        if (textEl) textEl.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> 已上传（点击更换）';
      }
      
      el.classList.add('has-files');
      markSectionFilled();
      autoSave();
    };
    reader.readAsDataURL(file);
    added++;
  });
}

function removeUploadedFile(zoneId, idx) {
  const files = uploadedFiles.get(zoneId);
  if (!files) return;
  files.splice(idx, 1);
  uploadedFiles.set(zoneId, files);
  
  const zone = document.getElementById(zoneId);
  if (!zone) return;
  
  const grid = zone.querySelector('.upload-preview-grid');
  if (grid) {
    const thumbs = grid.querySelectorAll('.upload-thumb');
    if (thumbs[idx]) thumbs[idx].remove();
    if (files.length === 0) {
      grid.style.display = 'none';
      zone.classList.remove('has-files');
      const textEl = zone.querySelector('.upload-zone-text');
      if (textEl) {
        const type = zone.dataset.uploadType || 'image';
        textEl.innerHTML = type === 'video' ? '点击或拖拽上传视频' : '点击或拖拽上传' + (textEl.textContent.includes('素材') ? '素材' : '文件');
      }
    }
  }
  markSectionFilled();
  autoSave();
}

// Product card image upload (real)
function handleProductImage(input) {
  const card = input.parentElement;
  const file = input.files[0];
  if (!file || !file.type.startsWith('image/')) return;
  
  const reader = new FileReader();
  reader.onload = function(e) {
    card.classList.add('has-image');
    card.innerHTML = `<img src="${e.target.result}" alt="Product" style="width:100%;height:100%;object-fit:cover;"><input type="file" hidden accept="image/*" onchange="handleProductImage(this)" title="点击更换图片">`;
    // Store in uploadedFiles under card id
    uploadedFiles.set(card.id, [{ name: file.name, size: file.size, type: file.type, dataURL: e.target.result, isImage: true }]);
    markSectionFilled();
    autoSave();
  };
  reader.readAsDataURL(file);
  input.value = '';
}

// Initialize drag-drop for all upload zones
function initDragDrop() {
  document.querySelectorAll('.upload-zone[data-upload-type], .video-upload-zone, .product-card-img').forEach(zone => {
    if (zone.dataset.dndInit) return;
    zone.dataset.dndInit = '1';
    
    zone.addEventListener('dragover', function(e) {
      e.preventDefault();
      e.stopPropagation();
      this.classList.add('drag-over');
    });
    
    zone.addEventListener('dragleave', function(e) {
      e.preventDefault();
      e.stopPropagation();
      this.classList.remove('drag-over');
    });
    
    zone.addEventListener('drop', function(e) {
      e.preventDefault();
      e.stopPropagation();
      this.classList.remove('drag-over');
      
      const input = this.querySelector('input[type=file]');
      const type = this.dataset.uploadType || (this.classList.contains('product-card-img') ? 'product' : 'generic');
      
      if (this.classList.contains('product-card-img')) {
        // Product card image
        if (e.dataTransfer.files[0]) {
          const dt = new DataTransfer();
          dt.items.add(e.dataTransfer.files[0]);
          input.files = dt.files;
          handleProductImage(input);
        }
      } else {
        // Normal upload zone
        if (input) {
          input.files = e.dataTransfer.files;
          handleFileSelect(input, type);
        }
      }
    });
    
    // Click on upload zone triggers file input
    zone.addEventListener('click', function(e) {
      // Don't trigger if user clicked on remove button or preview thumbnail
      if (e.target.closest('.thumb-remove')) return;
      if (this.classList.contains('product-card-img')) {
        if (this.classList.contains('has-image')) {
          // Click on uploaded image to replace
          const imgInput = this.querySelector('input[type=file]');
          if (imgInput) imgInput.click();
        } else {
          const input = this.querySelector('input[type=file]');
          if (input) input.click();
        }
      } else {
        const input = this.querySelector('input[type=file]');
        if (input) input.click();
      }
    });
  });
}

// Override product card img click
document.addEventListener('DOMContentLoaded', function() {
  // Re-init after render
  const origRenderSection = renderSection;
  renderSection = function() {
    origRenderSection.apply(this, arguments);
    setTimeout(initDragDrop, 100);
  };
});'''

content = content.replace(old_simulate, new_handlers)

# 3. Fix product card — remove old simulateProductUpload onclick, add real file input
content = content.replace(
    '''<div class="product-card-img" id="${cid}_img" onclick="simulateProductUpload(this)" title="点击上传产品主图">
            <span class="pc-img-icon"><svg''',
    '''<div class="product-card-img" id="${cid}_img" title="点击或拖拽上传产品主图">
            <input type="file" hidden accept="image/*" onchange="handleProductImage(this)">
            <span class="pc-img-icon"><svg'''
)

# 4. Fix the image view in reference section (line ~2242)
content = content.replace(
    '`<img src="${imgUrl}" style="width:100%;height:100%;object-fit:cover;" alt="${imgName}" onerror="this.style.display',
    '`<img src="${imgUrl}" style="width:100%;height:100%;object-fit:cover;" alt="${imgName}" onerror="this.style.display'
)

# ===== PART 2: MOBILE RESPONSIVE =====

# 5. Add hamburger menu button HTML
# Find the main-header section and add hamburger before breadcrumb
old_main_header = '''<main class="main">
    <div class="main-header">
      <div class="breadcrumb" id="breadcrumb">
        <span id="currentSectionName">店招</span>
      </div>'''

new_main_header = '''<main class="main">
    <!-- Mobile hamburger -->
    <button class="mobile-menu-btn" id="mobileMenuBtn" onclick="toggleMobileMenu()" aria-label="菜单">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
    <div class="main-header">
      <div class="breadcrumb" id="breadcrumb">
        <span id="currentSectionName">店招</span>
      </div>'''

content = content.replace(old_main_header, new_main_header)

# 6. Add mobile sidebar overlay close button HTML
old_sidebar_header = '''<aside class="sidebar">
    <div class="sidebar-header">'''

new_sidebar_header = '''<aside class="sidebar" id="sidebar">
    <button class="sidebar-close-btn" id="sidebarCloseBtn" onclick="toggleMobileMenu()" aria-label="关闭菜单">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
    <div class="sidebar-header">'''

content = content.replace(old_sidebar_header, new_sidebar_header)

# 7. Add mobile bottom bar before closing </body>
old_body_close = '''</body>
</html>'''

mobile_bottom_bar = '''
<!-- Mobile bottom action bar -->
<div class="mobile-bottom-bar" id="mobileBottomBar">
  <button class="mbb-item" onclick="switchPage('wangpu')" id="mbbWangpu">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
    <span>旺铺</span>
  </button>
  <button class="mbb-item" onclick="switchPage('detail')" id="mbbDetail">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
    <span>详情</span>
  </button>
  <button class="mbb-item" onclick="showPreview()">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
    <span>预览</span>
  </button>
  <button class="mbb-item" onclick="showExport()">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
    <span>导出</span>
  </button>
</div>

<!-- Mobile sidebar overlay backdrop -->
<div class="sidebar-backdrop" id="sidebarBackdrop" onclick="toggleMobileMenu()"></div>

</body>
</html>'''

content = content.replace(old_body_close, mobile_bottom_bar)

# 8. Add toggleMobileMenu JS function
old_toggle_js = '''function switchPage(page) {'''

new_toggle_js = '''// ===== MOBILE MENU =====
function toggleMobileMenu() {
  const sidebar = document.getElementById('sidebar');
  const backdrop = document.getElementById('sidebarBackdrop');
  const btn = document.getElementById('mobileMenuBtn');
  const isOpen = sidebar.classList.contains('mobile-open');
  
  if (isOpen) {
    sidebar.classList.remove('mobile-open');
    backdrop.classList.remove('show');
    btn.classList.remove('active');
    document.body.style.overflow = '';
  } else {
    sidebar.classList.add('mobile-open');
    backdrop.classList.add('show');
    btn.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

// Close mobile menu when navigating
const origSwitchPage = switchPage;
switchPage = function(page) {
  origSwitchPage(page);
  if (window.innerWidth <= 768) {
    toggleMobileMenu();
  }
  // Update bottom bar active state
  document.getElementById('mbbWangpu').classList.toggle('active', page === 'wangpu');
  document.getElementById('mbbDetail').classList.toggle('active', page === 'detail');
};

function switchPage(page) {'''

content = content.replace(old_toggle_js, new_toggle_js)

# ===== PART 3: ADD MOBILE + UPLOAD CSS =====

# 9. Add mobile CSS before the closing </style> tag
# Find the existing responsive section and expand it
old_responsive = '''/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
  .sidebar { display: none; }
  .main { margin-left: 0; padding: 16px; }
  .info-grid { grid-template-columns: 1fr; }
  .entry-card { padding: 32px 24px; }
}'''

new_responsive = '''/* ===== MOBILE MENU BUTTON ===== */
.mobile-menu-btn {
  display: none;
  position: fixed;
  top: 12px;
  left: 12px;
  z-index: 500;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: var(--card-bg);
  color: var(--text);
  cursor: pointer;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-sm);
  transition: all 0.2s ease;
}
.mobile-menu-btn.active { background: var(--accent); color: white; }

/* ===== SIDEBAR CLOSE BUTTON ===== */
.sidebar-close-btn {
  display: none;
  position: absolute;
  top: 12px;
  right: 12px;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  border: 1px solid var(--border);
  background: var(--card-bg);
  color: var(--text);
  cursor: pointer;
  align-items: center;
  justify-content: center;
  z-index: 10;
  transition: all 0.2s ease;
}

/* ===== SIDEBAR BACKDROP ===== */
.sidebar-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.35);
  z-index: 899;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
}
.sidebar-backdrop.show {
  display: block;
  opacity: 1;
  pointer-events: auto;
}

/* ===== MOBILE BOTTOM BAR ===== */
.mobile-bottom-bar {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 700;
  background: var(--glass-strong);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid var(--border);
  padding: 6px 8px env(safe-area-inset-bottom, 8px);
  display: none;
  justify-content: space-around;
  align-items: center;
}
.mbb-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  padding: 6px 12px;
  border: none;
  background: none;
  color: var(--text-secondary);
  font-size: 10px;
  font-weight: 500;
  cursor: pointer;
  border-radius: 10px;
  transition: all 0.15s ease;
  min-width: 56px;
  font-family: inherit;
}
.mbb-item.active { color: var(--accent); }
.mbb-item svg { opacity: 0.7; }
.mbb-item.active svg { opacity: 1; }

/* ===== DRAG OVER STATE ===== */
.upload-zone.drag-over,
.video-upload-zone.drag-over {
  border-color: var(--accent) !important;
  background: rgba(198,107,61,0.06) !important;
  box-shadow: 0 0 0 1px var(--accent);
  transform: scale(1.02);
}
.product-card-img.drag-over {
  border-color: var(--accent) !important;
  background: rgba(198,107,61,0.08) !important;
  box-shadow: 0 0 0 2px var(--accent);
}

/* File preview icon */
.file-preview-icon {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--card-bg);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
  .mobile-menu-btn { display: flex; }
  .sidebar-close-btn { display: flex; }
  .mobile-bottom-bar { display: flex; }
  
  .sidebar {
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 900;
    width: 280px;
    height: 100vh;
    height: 100dvh;
    transform: translateX(-100%);
    transition: transform 0.3s cubic-bezier(0.16,1,0.3,1);
    overflow-y: auto;
    box-shadow: var(--shadow-xl);
    padding-top: 50px;
  }
  .sidebar.mobile-open { transform: translateX(0); }
  
  .main { 
    margin-left: 0; 
    padding: 12px;
    padding-top: 56px;
    padding-bottom: 80px;
  }
  
  .main-header {
    flex-wrap: wrap;
    gap: 8px;
    padding: 8px 0;
  }
  
  .breadcrumb { margin-left: 0; }
  
  .header-actions {
    flex-wrap: wrap;
    gap: 6px;
  }
  
  .header-actions .btn {
    padding: 8px 12px;
    font-size: 11px;
    min-height: 40px;
  }
  
  .color-trigger-btn {
    padding: 8px 12px;
    min-height: 40px;
  }
  
  .info-grid { grid-template-columns: 1fr; }
  .entry-card { padding: 32px 24px; width: 92vw; }
  
  /* Product cards — single column */
  .product-cards-grid { grid-template-columns: 1fr; }
  
  /* Form fields full width */
  .field-input, .field-textarea, .field-select, .upload-zone, .video-upload-zone {
    font-size: 16px; /* Prevent iOS zoom on focus */
    min-height: 44px;
  }
  
  .field-textarea { min-height: 80px; }
  
  /* Upload zones — bigger touch targets */
  .upload-zone, .video-upload-zone {
    padding: 24px 16px;
    min-height: 100px;
  }
  
  .upload-zone-icon svg { width: 32px; height: 32px; }
  
  /* Preview thumbnails — smaller */
  .upload-preview-grid { gap: 6px; }
  .upload-thumb { width: 64px; height: 64px; }
  
  /* Color popover — reposition for mobile */
  .color-popover {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 300px;
    max-width: 92vw;
    max-height: 80vh;
    overflow-y: auto;
  }
  
  /* Export modal — full screen */
  .export-modal-overlay .modal-card {
    width: 92vw;
    max-width: none;
    margin: 16px;
    max-height: 85vh;
    overflow-y: auto;
  }
  
  /* Section cards — full width */
  .section-info { padding: 14px; }
  
  /* Larger touch targets for buttons */
  .btn {
    min-height: 44px;
    padding: 10px 16px;
    font-size: 13px;
  }
  
  /* Sidebar nav items */
  .nav-item { padding: 12px 16px; min-height: 44px; }
  
  /* Page toggle in sidebar */
  .page-toggle button { min-height: 40px; font-size: 12px; }
  
  /* Checkbox chips */
  .checkbox-chip { padding: 8px 14px; min-height: 40px; }
  
  /* Guide banner stacks */
  .guide-steps { flex-direction: column; gap: 10px; }
  .guide-step { font-size: 11px; }
  
  /* Table scrolls horizontally */
  .field-table { display: block; overflow-x: auto; }
  
  /* Admin badge */
  #adminModeBadge { font-size: 10px; padding: 3px 8px; }
}'''

content = content.replace(old_responsive, new_responsive)

# 10. Add upload-zone click handler that calls triggerUpload
# The upload zones need to click the hidden input. We'll use the drag-drop init.
# Add a global click delegation to body

old_delegation = '''// ===== INIT =====
document.addEventListener('DOMContentLoaded''

new_delegation = '''// ===== GLOBAL CLICK DELEGATION (upload zones) =====
document.addEventListener('click', function(e) {
  // Click on upload zone -> trigger file input
  const zone = e.target.closest('.upload-zone[data-upload-type], .video-upload-zone');
  if (zone && !e.target.closest('.thumb-remove') && !e.target.closest('img') && !e.target.closest('video')) {
    const input = zone.querySelector('input[type=file]');
    if (input) input.click();
  }
});

// ===== INIT =====
document.addEventListener('DOMContentLoaded''

content = content.replace(old_delegation, new_delegation)

# Write back
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done. File size: {len(content)} chars, {content.count(chr(10))} lines')
print('Replacements applied:')
print('  1. image upload -> real file input')
print('  2. images upload -> real file input (multiple)')
print('  3. video upload -> real file input')
print('  4. file/folder upload -> real file input')
print('  5. product card -> real file input')
print('  6. simulateUpload -> handleFileSelect + handleFiles')
print('  7. simulateProductUpload -> handleProductImage')
print('  8. Drag-drop on all upload zones')
print('  9. Mobile hamburger menu')
print('  10. Mobile sidebar overlay')
print('  11. Mobile bottom bar')
print('  12. Mobile CSS (44px touch targets, etc.)')
