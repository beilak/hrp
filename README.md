# hrp
### ToDo
ReadME is not ready


## k8s Deploy
Execute from deployment directory:


helm repo add stable https://charts.helm.sh/stable
helm repo update 
--helm install stable/nginx-ingress --name nginx-ingress --set controller.publishService.enabled=true


helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install hrp-ingress ingress-nginx/ingress-nginx --set controller.publishService.enabled=true --namespace home-rp

helm uninstall hrp-ingress --namespace home-rp     

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/aws/deploy.yaml --namespace home-rp

###Setup
1. helm repo add stable https://charts.helm.sh/stable
2. helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
3. helm repo update
4. For docker-desctop 
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/aws/deploy.yaml
5. 

# (helm repo add datawire https://www.getambassador.io)
# helm repo update


# istioctl operator init --watchedNamespaces istio-system --operatorNamespace istio-operator

# (helm repo add istio https://istio-release.storage.googleapis.com/charts)

# (helm repo update)

# (kubectl create namespace istio-system)

# (helm install istio-base istio/base -n istio-system --set defaultRevision=default)


helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
helm install istio-ingressgateway istio/gateway -n home-rp
helm delete istio-ingressgateway -n home-rp


kubectl create namespace istio-system
helm install istio-base istio/base -n istio-system --set defaultRevision=default
kubectl apply -f apigw/istio/istio.yaml



istioctl operator init --watchedNamespaces istio-system --operatorNamespace istio-operator
kubectl apply -f apigw/istio/istio.yaml
kubectl apply -f apigw/istio/routes.yaml -n home-rp


istioctl operator init --watchedNamespaces istio-system --operatorNamespace istio-operator
kubectl delete -f apigw/istio/istio.yaml
kubectl delete -f apigw/istio/routes.yaml -n home-rp



kubectl create namespace istio-ingress 
istioctl install -f apigw/istio/istio_ingress.yaml
istioctl uninstall -f apigw/istio/istio_ingress.yaml



kubectl create namespace nginx-ingress
helm install --version "3.35.0" -n nginx-ingress -f apigw/nginx_ingress/nginx.yaml \
ingress-nginx ingress-nginx/ingress-nginx



helm repo add traefik https://helm.traefik.io/traefik
helm repo update
kubectl create namespace traefik
helm install --version "10.1.2" -n traefik -f apigw/traefik/traefik.yaml traefik traefik/traefik

kubectl apply -f apigw/traefik/routes.yaml -n traefik
kubectl apply -f apigw/traefik/auth.yaml  -n traefik




[//]: # (kubectl create namespace istio-ingress)

[//]: # (helm install istio-ingressgateway istio/gateway -n istio-ingress)

[//]: # (k apply -f apigw/istio.yaml)

[//]: # ()
[//]: # (helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx)

[//]: # (helm repo update)

[//]: # ()
[//]: # (helm install --version "3.35.0" -n home-rp -f apigw/nginx.yaml \)

[//]: # (ingress-nginx ingress-nginx/ingress-nginx)




### NameSpace
0. NameSpace
   helm install home-rp ./homerp-namespace
   kubectl create namespace monitoring 

# Infrastructure
1. RabbitMQ 
   helm install mq oci://registry-1.docker.io/bitnamicharts/rabbitmq -f ./infra/rabbitmq/values.yaml --namespace home-rp
2. Redis
   helm install cache-redis oci://registry-1.docker.io/bitnamicharts/redis  -f ./infra/redis/values.yaml --namespace home-rp


### DB's:
1. Keycloak DB 
   helm install keycloakdb ./dbs/keycloakdb
2. OrgDB
   helm install org-db ./dbs/org_db
3. FinDB 
   helm install fin-db ./dbs/fin_db
   

### Services:
1. Install Org 
   helm install org ./org
   # ToDo Add waiting for DB init.
2. Install Fin 
   helm install fin ./fin
   # ToDo Add waiting for DB init.
3. Install Auth 
   helm install auth ./auth

### Ingerss:
1. Ingress
--   helm install ingress ./ingress
kubectl apply -f ingress/ingress.yaml

### Monitoring
      1. helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
      2. helm repo add stable https://charts.helm.sh/stable
      3. helm repo update

   1. helm install prom prometheus-community/kube-prometheus-stack -f ./monitoring/prometheus.yaml --atomic --namespace "monitoring"
   2. kubectl port-forward service/prom-grafana 9000:80 --namespace "monitoring"
   3. kubectl port-forward service/prom-kube-prometheus-stack-prometheus 9090  --namespace "monitoring"



Not working:
1. Keycloak 
   helm install keycloak ./idp/keycloak/




### Unistall all:   
   helm uninstall ingress
   helm uninstall org
   helm uninstall fin
   helm uninstall keycloak
   helm uninstall org-db
   helm uninstall fin-db 
   helm uninstall keycloakdb
   helm uninstall home-rp

   helm uninstall mq   --namespace home-rp
   helm uninstall cache-redis --namespace home-rp

   helm uninstall prom --namespace monitoring
   kubectl delete namespace monitoring





# HomeWork API

istioctl operator init --watchedNamespaces istio-system --operatorNamespace istio-operator


# (helm repo add datawire https://www.getambassador.io)
# (helm repo update)





-----DEL
kubectl delete -f ingress/ingress.yaml
kubectl delete  -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/aws/deploy.yaml    

helm uninstall hrp-ingress --namespace home-rp   
helm uninstall org
helm uninstall fin
helm uninstall org-db
helm uninstall fin-db

helm uninstall mq   --namespace home-rp
helm uninstall cache-redis --namespace home-rp

helm uninstall home-rp
kubectl delete namespace monitoring