from azure.identity import ClientSecretCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.mgmt.containerregistry.v2023_06_01_preview.models import Sku, SkuName, DebianArchivePackageSourceProperties, DebianArchiveProperties, Archive,ArchiveUpdateParameters

# Set your Azure subscription ID, resource group name, and container registry name
subscription_id = '48028acd-b54a-4a14-8e4c-a289a6ff61f9'
resource_group_name = 'pmctestrg0627'
registry_name = 'pmctestreg0909'
location = 'centraluseuap'  # Update with your desired location

# Put SP creds
client_id = 'b6051de3-36ef-437a-a47c-b93a34b4d742'
client_secret = ''
tenant_id = '72f988bf-86f1-41af-91ab-2d7cd011db47'

# Authenticate using the Service Principal credentials
credentials = ClientSecretCredential(tenant_id, client_id, client_secret)

# Specify the API version you want to use
api_version = "2023-06-01-preview" 

# Create the Container Registry Management Client
client = ContainerRegistryManagementClient(credentials, subscription_id, api_version=api_version)

archive_name = 'archive-ubuntu2110-0813-2'
# Create Archive version

debainArchiveSourceProperties = DebianArchivePackageSourceProperties(type="remote", url="https://packages.microsoft.com/ubuntu/21.10/prod", distribution_name="impish")
debainArchiveProperties = DebianArchiveProperties(package_source=debainArchiveSourceProperties,repository_endpoint_prefix="ubuntu/21.10.8.13.2/prod",distribution_name="impish")
archive = Archive(name=archive_name, properties=debainArchiveProperties,)
archive = client.archives.begin_create(resource_group_name, registry_name, 'debian', archive_name, archive_create_parameters = archive).result()
print(f"Archive endpoint {archive.properties.repository_endpoint}")

# Create Archive version

archive_version_name = 'archive-ubuntu2110-0813-2-pythonsdk-example-3'
print(f"Creating Archive version {archive_version_name}")
new_archive_version = client.archive_versions.begin_create(resource_group_name, registry_name, 'debian', archive_name, archive_version_name).wait(timeout=480).result()
print(f"Version: {new_archive_version.name} state {new_archive_version.provisioning_state}")


# Publish Archive version
print(f"Updating Archive {archive_name} with version {archive_version_name}")
archiveppdateparameters = ArchiveUpdateParameters(published_version=archive_version_name);
client.archives.update(resource_group_name, registry_name, 'debian', archive_name,archiveppdateparameters);

# Create Another Archive version

# Create Archive version

archive_version_name_2 = 'archive-ubuntu2110-0813-2-pythonsdk-example-3-2'
print(f"Creating Archive version {archive_version_name_2}")
new_archive_version = client.archive_versions.begin_create(resource_group_name, registry_name, 'debian', archive_name, archive_version_name_2).wait(timeout=480).result()
print(f"Version: {archive_version_name_2.name} state {archive_version_name_2.provisioning_state}")


# List Archives
archives = client.archives.list(resource_group_name, registry_name, 'debian')



# List Archives Versions
for archive in archives:
    print(f"Archive: {archive.name}")
    archiveVersions = client.archive_versions.list(resource_group_name, registry_name, 'debian', archive.name)
    for archiveVersion in archiveVersions:
        print(f"Version: {archiveVersion.name} state {archiveVersion.provisioning_state}")

# Delete Archive versions


# Delete Archive


