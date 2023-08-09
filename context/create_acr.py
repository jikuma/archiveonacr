from azure.identity import ClientSecretCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.mgmt.containerregistry.models import Sku, SkuName

# Set your Azure subscription ID, resource group name, and container registry name
subscription_id = '48028acd-b54a-4a14-8e4c-a289a6ff61f9'
resource_group_name = 'pmctestrg0627'
registry_name = 'pmctestreg0627'
location = 'centraluseuap'  # Update with your desired location

# Put SP creds
client_id = 'b6051de3-36ef-437a-a47c-b93a34b4d742'
client_secret = '<client secret>'
tenant_id = '72f988bf-86f1-41af-91ab-2d7cd011db47'

# Authenticate using the Service Principal credentials
credentials = ClientSecretCredential(tenant_id, client_id, client_secret)

# Specify the API version you want to use
api_version = "2023-06-01-preview" 

# Create the Container Registry Management Client
client = ContainerRegistryManagementClient(credentials, subscription_id, api_version=api_version)

# List Archives
# archives = client.archives.list(resource_group_name, registry_name, 'debian')

# List Archives Versions
#for archive in archives:
#    print(f"Archive: {archive.name}")
#    archiveVersions = client.archive_versions.list(resource_group_name, registry_name, 'debian', archive.name)
#    for archiveVersion in archiveVersions:
#        print(f"Version: {archiveVersion.name} state {archiveVersion.provisioning_state}")

# Create Archive version

archive_name = 'archive-ubuntu2110'
archive_version_name = 'archive-ubuntu2110-pythonsdk-example-2'

new_archive_version = client.archive_versions.begin_create(resource_group_name, registry_name, 'debian', archive_name, archive_version_name).wait(timeout=420).result()

print(f"Version: {new_archive_version.name} state {new_archive_version.provisioning_state}")
