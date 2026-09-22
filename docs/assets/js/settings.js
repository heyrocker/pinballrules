(function() {
  const root = document.documentElement;

  // === Dark Mode ===
  if (localStorage.getItem('dark-mode') === 'true') {
    root.classList.add('dark-mode');
  }

  const dmButtons = document.querySelectorAll('.dm-toggle');
  dmButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      const mode = btn.getAttribute('data-mode');
      if (mode === 'on') {
        root.classList.add('dark-mode');
        localStorage.setItem('dark-mode', 'true');
      } else {
        root.classList.remove('dark-mode');
        localStorage.setItem('dark-mode', 'false');
      }
      updateDMStates();
    });
  });

  function updateDMStates() {
    const isDark = root.classList.contains('dark-mode');
    dmButtons.forEach(function(btn) {
      const mode = btn.getAttribute('data-mode');
      btn.classList.toggle('active', (mode === 'on') === isDark);
    });
  }

  // === Font Size ===
  const savedSize = localStorage.getItem('font-size');
  if (savedSize) {
    root.classList.add('font-size-' + savedSize);
  }

  const fsButtons = document.querySelectorAll('.font-size-btn');
  fsButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      const size = btn.getAttribute('data-size');
      // Remove all font-size classes
      for (let i = 1; i <= 5; i++) {
        root.classList.remove('font-size-' + i);
      }
      if (size !== '1') {
        root.classList.add('font-size-' + size);
      }
      localStorage.setItem('font-size', size);
      updateFSStates();
    });
  });

  function updateFSStates() {
    const current = localStorage.getItem('font-size') || '1';
    fsButtons.forEach(function(btn) {
      btn.classList.toggle('active', btn.getAttribute('data-size') === current);
    });
  }

  // Initial state
  updateDMStates();
  updateFSStates();
})();   