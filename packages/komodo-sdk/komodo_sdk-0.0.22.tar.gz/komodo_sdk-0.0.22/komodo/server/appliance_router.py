from fastapi import Depends, APIRouter, HTTPException

from komodo.core.utils.indexer import Indexer
from komodo.models.framework.runners import get_all_agents
from komodo.server.globals import get_appliance
from komodo.store.collection_store import CollectionStore

router = APIRouter(
    prefix='/api/v1/appliance',
    tags=['Appliance']
)


@router.get('/description', response_model=dict, summary='Get appliance description',
            description='Get the description of the appliance.')
def get_appliance_description(appliance=Depends(get_appliance)):
    if not appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")

    agents = get_all_agents(appliance)
    return {
        "shortcode": appliance.shortcode,
        "name": appliance.name,
        "purpose": appliance.purpose,
        "agents": [a.to_dict() for a in agents]
    }


@router.get('/index', summary='Index all data sources',
            description='Index all data sources for the appliance.')
def index_all_data_sources(appliance=Depends(get_appliance)):
    if not appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")

    qdrant = appliance.get_vector_store()
    collection = appliance.get_collection()
    indexer = Indexer(qdrant, collection.guid)
    indexer.run(max_updates=1, update_interval=5)
    return {"status": "success"}


@router.get('/reindex', summary='Re-index all data sources.',
            description='Deletes all existing data and re-indexes all data sources for the appliance.')
def re_index_all_data_sources(appliance=Depends(get_appliance)):
    if not appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")

    qdrant = appliance.get_vector_store()
    collection = appliance.get_collection()

    qdrant.delete_all()
    store = CollectionStore()
    store.remove_collection(collection.guid)

    collection = appliance.get_collection()
    indexer = Indexer(qdrant, collection.guid)
    indexer.run(max_updates=1, update_interval=5)
    return {"status": "success"}
