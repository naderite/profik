// src/serviceWorker.js

import { Workbox } from 'workbox-window';

export function registerServiceWorker() {
  if ('serviceWorker' in navigator) {
    const workbox = new Workbox('/service-worker.js');
    workbox.register();
  }
}
