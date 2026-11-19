// Looping videos load and play only when on screen; still for reduced motion.
(function () {
  var vids = document.querySelectorAll('video.loop-video');
  if (!vids.length) return;
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  vids.forEach(function (v) { v.muted = true; v.playsInline = true; if (still) v.controls = true; });
  if (still) return;
  if (!('IntersectionObserver' in window)) { vids.forEach(function (v) { v.play().catch(function(){}); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.play().catch(function(){}); } else { e.target.pause(); }
    });
  }, { rootMargin: '200px 0px' });
  vids.forEach(function (v) { io.observe(v); });
})();
