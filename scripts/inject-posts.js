async function loadPosts() {
  try {
    const response = await fetch('/blog/posts.json');
    const posts = await response.json();

    const postList = document.getElementById('post-list');
    postList.innerHTML = '';

    // Filter out hidden posts
    const visiblePosts = posts.filter(p => !p.hidden);

    // Sort newest first
    visiblePosts.sort((a, b) => new Date(b.date) - new Date(a.date));

    visiblePosts.forEach(post => {
      const li = document.createElement('li');

      const formattedDate = post.date.toLowerCase() !== 'in-progress'
        ? new Date(post.date).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
          })
        : 'In Progress';

      li.innerHTML = `
        <a href="${post.url}" class="d-block text-decoration-none">
          <h3 class="mb-1">${post.title}</h3>
          <time datetime="${post.date}" class="d-block mb-2 text-secondary">${formattedDate}</time>
          ${post.description ? `<p class="text-light small mb-2">${post.description}</p>` : ''}
          ${
            post.tags && post.tags.length
              ? `<div class="mt-2">${post.tags
                  .map(tag => `<span class="badge bg-primary me-1">${tag}</span>`)
                  .join('')}</div>`
              : ''
          }
        </a>
      `;

      postList.appendChild(li);
    });
  } catch (err) {
    console.error('Error loading posts:', err);
  }
}

loadPosts();
