# hrp

## k8s Deploy
Execute from deployment directory:

### NameSpace
0. NameSpace
   helm install home-rp ./homerp-namespace
   kubectl create namespace monitoring 

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
2. FinDB 
   helm install fin ./fin

### Ingerss:
1. Ingress
   helm install ingress ./ingress


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

   helm uninstall prom --namespace monitoring
   kubectl delete namespace monitoring
