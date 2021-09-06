build_mlflow_image:
	docker image build -t antonio/mlflow:1.19 -f 'Dockerfile_mlflow' .

run_mlflow_image_local:build_mlflow_image
	docker run -d --name mlflow1.19 -p 5000:5000 antonio/mlflow\:1.19

build_model_image:
	docker image build -t antonio/irismodel:1.0 -f 'Dockerfile_model' .

run_model_image_local:build_model_image
	docker run -d --name irismodel1.0 -p 8000:8000 antonio/irismodel\:1.0

push_mlflow_image_acr:
	az login -u $AZURE_USER -p $AZURE_PW
	az acr login --name antoniocontreg --password $CONT_REGISTRY_PW
	docker login antoniocontreg.azurecr.io
	docker tag antonio/mlflow:1.19 antoniocontreg.azurecr.io/mlflow
	docker push antoniocontreg.azurecr.io/mlflow

run_mlflow_image:
	az container create \
	--resource-group DS_EU_Internal_Proj_01 \
	--name aciantoniomlflow \
	--image antoniocontreg.azurecr.io/mlflow:latest \
	--dns-name-label antoniomlflowaci \
	--ip-address public \
	--ports 5000 \
	--registry-username antoniocontreg
	--registry-password $CONT_REGISTRY_PW

push_model_image_acr:
	az login -u $AZURE_USER -p $AZURE_PW
	az acr login --name antoniocontreg
	docker login antoniocontreg.azurecr.io
	docker tag antonio/irismodel:1.0 antoniocontreg.azurecr.io/irismodel
	docker push antoniocontreg.azurecr.io/irismodel

restart_model_acr: #boots up with image tagged as latest
	az container restart \
	--name aciantonioirismodel \
	--resource-group DS_EU_Internal_Proj_01

run_model_image:
	az container create \
	--resource-group DS_EU_Internal_Proj_01 \
	--name aciantonioirismodel \
	--image antoniocontreg.azurecr.io/irismodel:latest \
	--dns-name-label antonioirismodelaci \
	--ip-address public \
	--ports 8000 \
	--registry-username antoniocontreg \
	--registry-password $CONT_REGISTRY_PW
