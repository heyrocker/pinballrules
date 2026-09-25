(function() {
  const root = document.documentElement;

  // The inline script in the layout <head> sets the starting theme.
  const dmToggle = document.getElementById('dark-mode-toggle');

  function updateDMStates() {
    if (!dmToggle) return;
    dmToggle.setAttribute('aria-pressed', root.classList.contains('dark-mode'));
  }

  if (dmToggle) {
    dmToggle.addEventListener('click', function() {
      const isDark = root.classList.toggle('dark-mode');
      try { localStorage.setItem('dark-mode', isDark); } catch (e) {}
      updateDMStates();
    });
  }

  updateDMStates();
})();
