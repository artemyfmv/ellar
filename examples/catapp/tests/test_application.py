import os
import pytest

from pathlib import Path
from catapp.application.cats.routers import cat_router

from architek.core.testclient import TestClientFactory

os.environ.setdefault('ARCHITEK_CONFIG_MODULE',  'app_module_test.tests.settings')

BASEDIR = Path(__file__).resolve().parent.parent

test_client = TestClientFactory.create_test_module(
    routers=[cat_router],
    template_folder='views',
    static_folder='statics',
    base_directory=os.path.join(BASEDIR, 'application', 'cats')
).get_client()

# test_client = TestClientFactory.create_testing_module_from_module(
#     module=ItemModule
# ).create_test_client()


@pytest.mark.asyncio
async def test_cat_router():
    with test_client as client:
        response = client.get('/cats-router/html')
        assert response.status_code == 200
