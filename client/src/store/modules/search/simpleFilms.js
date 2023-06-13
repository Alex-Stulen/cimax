import { buildApiEndpoint } from "../../../conf/settings";
import { defaultPageSize } from "../../../components/films/config";


export default {
  state() {
    return {
      search: "",
      filmsPageData: {
        count: 0,
        next: '',
        previous: null,
        results: [],
        currentPage: 1
      }
    };
  },
  actions: {
    async getFilmByIdApi(context, id){
      const url = buildApiEndpoint(`/simple-films/${id}`)
      const response = await fetch(url)
      if(response.ok){
        return await response.json()
      }
      else{
        return {
          status: 'fail',
          code: response.status
        }
      }
    },
    async setFilmsPageDataApi(context, data){
      let url = buildApiEndpoint(`/simple-films/`)
      
      let queryArray = []

      if(data.page){
        queryArray.push(`page=${data.page}`)
      }

      if(data.pageSize){
        queryArray.push(`page_size=${data.pageSize}`)
      }
      else{
        queryArray.push(`page_size=${defaultPageSize}`)
      }
      
      if(data.search){
        queryArray.push(`search=${data.search}`)
      }

      let query = ''
      if(queryArray.length > 0){
        query = queryArray.join('&')
      }


      url = url + '?' + query
      const response = await fetch(url)
      if(response.ok){
        const response_json = await response.json()
        const newData = {
          currentPage: data.page ? data.page : 1,
          ...response_json
        }
        context.commit('setFilmsPageData', newData)
        return response_json
      }
      else{
        return {
          'status': 'fail',
          'code': response.status
        }
      }
    }
  },
  mutations: {
    setSearch(state, newSearch) {
      state.search = newSearch;
      return state.search
    },
    setFilmsPageData(state, newFilmsPageData){
      state.filmsPageData = newFilmsPageData
      return state.filmsPageData
    }
  },
  getters: {
    getCurrentSearch(state) {
      return state.search;
    },
    getFilmsPageData(state){
      return state.filmsPageData
    }
  },
};
