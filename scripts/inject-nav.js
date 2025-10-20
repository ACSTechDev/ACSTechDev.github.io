async function injectHTML(selector, file) {
  try {
    const response = await fetch(file);
    if (!response.ok) throw new Error(`Failed to load ${file}`);
    const html = await response.text();
    document.querySelector(selector).innerHTML = html;
  } catch (err) {
    console.error(err);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  injectHTML('#site-header', '/components/header.html');
  injectHTML('#site-footer', '/components/footer.html');
});
