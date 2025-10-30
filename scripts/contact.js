document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contact-form");
  if (form) {
    const formspreeID = "webcontact";  
    form.action = `https://api.acstech.dev/f/${formspreeID}`;
    
    form.addEventListener('submit', (e) => {
      const hp = form.querySelector('input[name="hp"]');
      if (hp && hp.value) {
        e.preventDefault();
        return;
      }
  }
});
