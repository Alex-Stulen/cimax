export const DEBUG = import.meta.env.DEV;


const env = import.meta.env;
export let SERVER_HOST = env.VITE_SERVER_SCHEMA + '://' + env.VITE_SERVER_HOST

if(import.meta.env.VITE_SERVER_URL_WITH_PORT === 'true'){
    SERVER_HOST = SERVER_HOST + ':' + env.VITE_SERVER_PORT
}

const API_VERSION = 'v1'

export function buildApiEndpoint(endpoint){
    if(!endpoint.startsWith('/')){
        endpoint = '/' + endpoint
    }
    return `${SERVER_HOST}/api/${API_VERSION}${endpoint}`
}
