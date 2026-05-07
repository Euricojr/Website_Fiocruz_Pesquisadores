
/**
 * dashboard.js - UI logic for the INSIGHT Admin Dashboard.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Auth Check
    const userName = localStorage.getItem('user_name');
    if (!localStorage.getItem('access_token')) {
        window.location.href = 'index.html';
    }
    document.getElementById('user-display-name').innerText = userName || 'Usuário';

    // Logout
    document.getElementById('logout-btn').addEventListener('click', () => {
        localStorage.clear();
        window.location.href = 'index.html';
    });

    // Navigation
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.section');
    const sectionTitle = document.getElementById('section-title');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const target = item.getAttribute('data-section');
            
            navItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');

            sections.forEach(s => s.classList.remove('active'));
            document.getElementById(target).classList.add('active');
            
            sectionTitle.innerText = item.querySelector('span').innerText;
            
            // Load section data
            loadSectionData(target);
        });
    });

    // Initial Load
    loadSectionData('publications');

    // Sync Publications Button
    const syncPubsBtn = document.getElementById('sync-pubs-btn');
    if (syncPubsBtn) {
        syncPubsBtn.addEventListener('click', async () => {
            syncPubsBtn.disabled = true;
            syncPubsBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sincronizando...';
            
            try {
                const res = await API.post('/publications/sync', {});
                alert(res.message);
                if (res.success) {
                    loadSectionData('publications');
                }
            } catch (err) {
                alert('Erro ao sincronizar publicações.');
            } finally {
                syncPubsBtn.disabled = false;
                syncPubsBtn.innerHTML = '<i class="fas fa-sync"></i> Sincronizar Lattes/Scholar';
            }
        });
    }

    // Forms handling
    setupForm('form-publication', '/publications/', 'publications');
    setupForm('form-project', '/projects/', 'projects');
    setupForm('form-team', '/team/member', 'team');

    // Special handling for Upload
    const uploadForm = document.getElementById('form-upload');
    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const fileInput = document.getElementById('upload-file');
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        try {
            const res = await API.request('/uploads/image', {
                method: 'POST',
                body: formData
            });
            if (res.success) {
                alert('Imagem enviada!');
                loadSectionData('images');
                uploadForm.reset();
            }
        } catch (err) {
            alert('Erro ao enviar imagem.');
        }
    });
});

async function loadSectionData(section) {
    switch(section) {
        case 'publications':
            const pubs = await API.get('/publications/');
            renderPublications(pubs);
            break;
        case 'projects':
            const projs = await API.get('/projects/');
            renderProjects(projs);
            break;
        case 'team':
            const team = await API.get('/team/');
            renderTeam(team);
            break;
        case 'images':
            const imgs = await API.get('/uploads/images');
            renderImages(imgs);
            break;
    }
}

function renderPublications(data) {
    const tbody = document.querySelector('#table-publications tbody');
    tbody.innerHTML = '';
    data.forEach((pub, index) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><strong>${pub.title}</strong><br><small>${pub.authors}</small></td>
            <td>${pub.year}</td>
            <td><span class="tag">${pub.category}</span></td>
            <td>
                <button class="btn btn-small btn-danger" onclick="deleteItem('/publications/${index}', 'publications')">
                    <i class="fas fa-trash"></i>
                </button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function renderProjects(data) {
    const container = document.getElementById('list-projects');
    container.innerHTML = '';
    data.forEach((proj, index) => {
        const div = document.createElement('div');
        div.className = 'project-card';
        div.innerHTML = `
            <img src="${proj.image || 'https://via.placeholder.com/300x180?text=Sem+Imagem'}" class="project-img" onerror="this.src='https://via.placeholder.com/300x180?text=Erro+Imagem'">
            <div class="project-body">
                <h4>${proj.title}</h4>
                <p style="font-size: 0.85rem; color: #718096; margin: 0.5rem 0;">${proj.description}</p>
                <div>${proj.tags.map(t => `<span class="tag">${t}</span>`).join('')}</div>
                <button class="btn btn-small btn-danger" style="margin-top: 1rem" onclick="deleteItem('/projects/${index}', 'projects')">Remover</button>
            </div>
        `;
        container.appendChild(div);
    });
}

function renderTeam(data) {
    const container = document.getElementById('list-team');
    container.innerHTML = '';

    // Populate category datalist with existing categories
    const datalist = document.getElementById('team-categories');
    if (datalist) {
        datalist.innerHTML = '';
        data.forEach(catGroup => {
            const option = document.createElement('option');
            option.value = catGroup.category;
            datalist.appendChild(option);
        });
    }
    
    data.forEach((catGroup, catIndex) => {
        const section = document.createElement('div');
        section.className = 'card';
        section.innerHTML = `
            <h4 style="margin-bottom: 1rem; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;">${catGroup.category}</h4>
            <div class="grid" style="grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));">
                ${catGroup.members.map((m, mIndex) => `
                    <div style="text-align: center; padding: 1rem; border: 1px solid #eee; border-radius: 0.5rem;">
                        <img src="${m.image || 'https://via.placeholder.com/80?text=👤'}" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; margin-bottom: 0.5rem;">
                        <h5 style="margin-bottom: 0.2rem;">${m.name}</h5>
                        <p style="font-size: 0.75rem; color: #718096;">${m.role}</p>
                        <button class="btn btn-small btn-danger" style="margin-top: 0.5rem" onclick="deleteItem('/team/member/${catIndex}/${mIndex}', 'team')">Remover</button>
                    </div>
                `).join('')}
            </div>
        `;
        container.appendChild(section);
    });
}

function renderImages(data) {
    const container = document.getElementById('gallery');
    container.innerHTML = '';
    data.forEach(img => {
        const div = document.createElement('div');
        div.className = 'gallery-item';
        div.innerHTML = `
            <img src="${img.url}">
            <div class="gallery-overlay">
                <button class="btn btn-small btn-primary" onclick="copyToClipboard('${img.url}')" title="Copiar Link">
                    <i class="fas fa-link"></i>
                </button>
                <button class="btn btn-small btn-danger" onclick="deleteItem('/uploads/image/${img.filename}', 'images')" title="Deletar">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        `;
        container.appendChild(div);
    });
}

function setupForm(formId, endpoint, section) {
    const form = document.getElementById(formId);
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        // Handle tags for projects
        if (data.tags) {
            data.tags = data.tags.split(',').map(t => t.trim());
        }

        try {
            const res = await API.post(endpoint, data);
            if (res.success) {
                alert('Adicionado com sucesso!');
                form.reset();
                loadSectionData(section);
            }
        } catch (err) {
            alert('Erro ao adicionar item.');
        }
    });
}

async function deleteItem(endpoint, section) {
    if (confirm('Deseja realmente remover este item?')) {
        try {
            const res = await API.delete(endpoint);
            if (res.success) {
                loadSectionData(section);
            }
        } catch (err) {
            alert('Erro ao remover item.');
        }
    }
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert('URL copiada para a área de transferência!');
    });
}

// Global exposure for onclick handlers
window.deleteItem = deleteItem;
window.copyToClipboard = copyToClipboard;
