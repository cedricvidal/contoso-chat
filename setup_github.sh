#!/bin/bash

set -ex

echo "Reading config.json file for PromptFlow usage..."
subscriptionId=$(cat config.json | jq -r .subscription_id)
rgname=$(cat config.json | jq -r .resource_group)
workspace_name=$(cat config.json | jq -r .workspace_name)

echo "subscriptionId: ${subscriptionId}"
echo "rgname: ${rgname}"
echo "workspace_name: ${workspace_name}"

userAssignedId=contoso-chat-mvpsummit
keyvault=$(az ml workspace show --name ${workspace_name} -g ${rgname} | jq -r '.key_vault | split("/") | last')

# az login
# az account set -s $subscriptionId

# Create a user-assigned managed identity
az identity create -g $rgname -n $userAssignedId --query "id"

# Get id, principalId of user-assigned managed identity
um_details=$(az identity show -g $rgname -n $userAssignedId --query "[id, clientId, principalId]")

# Get id of user-assigned managed identity
user_managed_id="$(echo $um_details | jq -r '.[0]')"

# Get principal Id of user-assigned managed identity
principalId="$(echo $um_details | jq -r '.[2]')"

# Grant the user managed identity permission to access the workspace (AzureML Data Scientist)
az role assignment create --assignee $principalId --role "AzureML Data Scientist" --scope "/subscriptions/$subscriptionId/resourcegroups/$rgname/providers/Microsoft.MachineLearningServices/workspaces/$workspace_name"

# Grant the user managed identity permission to access the workspace keyvault (get and list)
az keyvault set-policy --name $keyvault --resource-group $rgname --object-id $principalId --secret-permissions get list
