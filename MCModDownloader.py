from MCSiteAPI import ModrinthAPI
from MCSiteAPI import CurseforgeAPI
from MCSiteAPI import utils
from typing import Union, Literal
from furl import furl
import os



class MCModDownloader:
    def __init__(self):
        self.modrinth_api = ModrinthAPI()
        self.curseforge_api = CurseforgeAPI()
        self.utils = MCM_Utils()



    async def download_latest(self, url: str, parameters: dict=None):

        host = await self.utils.get_host(url)
        filename = metadata = files = None
        
        async def getModData(API: object):
            modData = await API.get_project(url)
            metadata, files = await API.download(url, parameters=parameters)

            return modData, metadata, files

        match host:
            case "modrinth.com":
                MDAPI = self.modrinth_api  
                modData, metadata, files = await getModData(MDAPI)
                filename = f"{modData['slug']}_{metadata['version_number']}.jar"  
            
            case "www.curseforge.com":
                CFAPI = self.curseforge_api
                modData, metadata, files = await getModData(CFAPI)
                filename = f"{modData['slug']}_{metadata['id']}.jar"

        return filename, files, metadata, host



    async def saveFile(self, file: bytes, name: str, path: str):
        try:
            modPath = os.path.join(path, "mods")
            os.makedirs(modPath, exist_ok=True)
            finalPath = os.path.join(modPath, name)
            with open(finalPath, "wb") as f:
                f.write(file)
        except Exception as e:
            print(f"Error saving file: {e}")





class MCM_Utils:
    def __init__(self):
        self.modrinth_api = ModrinthAPI()
        self.curseforge_api = CurseforgeAPI()



    async def get_equivalent_ids(self, id: Union[str, int], host: Literal['modrinth.com', 'www.curseforge.com']):
        CFId = MDId = None

        match host:
            case "modrinth.com":   
                MDId = id['project_id']
                project = await self.modrinth_api.get_project_by_id(MDId)
                if project.get('slug'):
                    CFId = await self.curseforge_api.get_id_by_slug(project['slug'])
            case "www.curseforge.com":
                CFId = id['modId']
                project = await self.curseforge_api.get_project_by_id(CFId)
                if project.get('slug'):
                    mdProject = await self.modrinth_api.get_project_by_id(project['slug'])
                    if mdProject is not None:
                        MDId = mdProject['id']
        print(f"Equivalent ID's: {MDId}, {CFId}")
        return [MDId, CFId]
    
    
    
    async def getSpecifiedData(self, dep: str, dataTypes: tuple[str, str]):
        async def getData(api: object, name: str, id: str):
            project = await api.get_project_by_id(id, retries=20)
            return project[name]
                
        data = None
        if dep[0] is not None:
            data = await getData(self.modrinth_api, dataTypes[0], dep[0])
        else:
            data = await getData(self.curseforge_api, dataTypes[1], dep[1])
            
        return data
    
    
    
    async def returnModName(self, data: any, host: Literal['modrinth.com', 'www.curseforge.com']):
        async def getModName(API: object, id: Union[str, int]):
            project = await API.get_project_by_id(id)
            return project

        match host:
            case "modrinth.com":
                id = data[0]['project_id']
                metadata = await getModName(self.modrinth_api, id)
                return metadata['title']
            case "www.curseforge.com":
                id = data[0]['modId']
                metadata = await getModName(self.curseforge_api, id)
                return metadata['name']
    
    
    
    async def get_host(self, url: str):
        f = furl(url)
        host = f.host

        return(host)  