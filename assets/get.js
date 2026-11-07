// Smart download link: sends iPhones to the App Store and Android phones to
// Google Play. Anything else (desktop, unknown) stays on the page, which shows
// both store buttons. Optional ?s=<source> (e.g. ?s=tiktok) is passed to Google
// Play as utm_source so Play Console can report where installs came from.
(function () {
  var body = document.body;
  var ios = body.getAttribute('data-ios');
  var android = body.getAttribute('data-android');
  var ua = navigator.userAgent || '';
  var isIOS = /iPhone|iPad|iPod/i.test(ua) ||
    (/Macintosh/i.test(ua) && navigator.maxTouchPoints > 1);
  var isAndroid = /Android/i.test(ua);

  var source = new URLSearchParams(location.search).get('s');
  if (source && /^[\w-]{1,40}$/.test(source)) {
    android += '&referrer=' + encodeURIComponent('utm_source=' + source + '&utm_medium=social');
    document.querySelector('[data-store="android"]').href = android;
  }

  if (isIOS) location.replace(ios);
  else if (isAndroid) location.replace(android);
  else document.querySelector('.eyebrow').textContent = 'Free download';
})();
