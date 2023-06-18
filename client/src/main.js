import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store';


import PrimeVue from 'primevue/config';

import "/node_modules/primeflex/primeflex.css"
import "primevue/resources/themes/viva-dark/theme.css";  
import "primevue/resources/primevue.min.css";
import 'primeicons/primeicons.css';


import "video.js/dist/video-js.css";

const app = createApp(App)

app.use(router)
app.use(store)
app.use(PrimeVue)

app.mount('#app')
