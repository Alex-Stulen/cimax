import { createStore } from "vuex"
import simpleFilmsStore from './modules/search/simpleFilms';

export default createStore({
    modules:{
        simpleFilmsStore,
    }
})