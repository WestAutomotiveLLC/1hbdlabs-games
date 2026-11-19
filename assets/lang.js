// Picks the homepage language for each visitor.
// First visit to the English homepage: if the browser's language is Spanish, French, Korean or Filipino/Tagalog,
// go to that language's homepage. The EN/ES/FIL/FR/KO links in the header are the backup: tapping one
// remembers the choice, so the site stops switching for that visitor.
(function () {
  var KEY = '1hbd-lang';
  var LANGS = { es: 'es', fr: 'fr', ko: 'ko', tl: 'tl', fil: 'tl' };

  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('[data-setlang]');
    if (a) { try { localStorage.setItem(KEY, a.getAttribute('data-setlang')); } catch (_) {} }
  }, true);

  var script = document.currentScript;
  if (!script || !script.hasAttribute('data-home-redirect')) return;

  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (_) {}
  var target = saved;
  if (!target) {
    var list = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || ''];
    for (var i = 0; i < list.length && !target; i++) {
      var code = String(list[i] || '').toLowerCase();
      if (code.indexOf('en') === 0) target = 'en';
      else {
        for (var k in LANGS) if (code.indexOf(k) === 0) { target = LANGS[k]; break; }
      }
    }
  }
  if (target && target !== 'en' && LANGS[target]) location.replace(LANGS[target] + '/' + location.hash);
})();
