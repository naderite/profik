let mathJaxPromise;

export function loadMathJax() {
  if (!mathJaxPromise) {
    mathJaxPromise = new Promise((resolve) => {
      const mathJaxScript = document.createElement("script");
      mathJaxScript.src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js";
      mathJaxScript.async = true;
      mathJaxScript.onload = resolve;
      document.head.appendChild(mathJaxScript);
    });
  }

  return mathJaxPromise;
}
