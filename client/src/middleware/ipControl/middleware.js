import { buildApiEndpoint } from '../../conf/settings.js'

export default async function ipControlMiddleware({ to, router }){
    if(to.name === '403'){
        return true
    }

    const checkIpAssessUrl = buildApiEndpoint('/ip-controls/is-allowed-ip/')
    try{
        const response = await fetch(checkIpAssessUrl)
        if(response.status === 200){
            return true
        }
        else{
            router.push('/403')
        }
    }
    catch (error){
        router.push('/403')
    }
}
