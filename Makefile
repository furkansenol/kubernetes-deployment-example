start:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
	kubectl apply -f .\app\deployment.yaml
	kubectl apply -f .\app\service.yaml
	kubectl apply -f .\app\ingress-class.yaml
	kubectl apply -f .\app\ingress.yaml

stop:
	kubectl delete all -l app=hello-world-app
