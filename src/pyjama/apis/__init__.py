# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from ..api.abstractitems_api import AbstractitemsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ..api.abstractitems_api import AbstractitemsApi
from ..api.activities_api import ActivitiesApi
from ..api.attachments_api import AttachmentsApi
from ..api.baselines_api import BaselinesApi
from ..api.comments_api import CommentsApi
from ..api.files_api import FilesApi
from ..api.filters_api import FiltersApi
from ..api.items_api import ItemsApi
from ..api.itemtypes_api import ItemtypesApi
from ..api.picklistoptions_api import PicklistoptionsApi
from ..api.picklists_api import PicklistsApi
from ..api.projects_api import ProjectsApi
from ..api.relationships_api import RelationshipsApi
from ..api.relationshiptypes_api import RelationshiptypesApi
from ..api.releases_api import ReleasesApi
from ..api.system_api import SystemApi
from ..api.tags_api import TagsApi
from ..api.testcycles_api import TestcyclesApi
from ..api.testplans_api import TestplansApi
from ..api.testruns_api import TestrunsApi
from ..api.usergroups_api import UsergroupsApi
from ..api.users_api import UsersApi
