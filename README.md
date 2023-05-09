# hrp



## k8s Deploy
Execute from deployment directory:

### NameSpace
0. NameSpace
   helm install home-rp ./homerp-namespace

### DB's:
1. Keycloak DB 
   helm install keycloakdb ./dbs/keycloakdb
2. OrgDB
   helm install org-db ./dbs/org_db

### Services:
1. Install Org 
   helm install org ./org
   # ToDo Add waiting for DB init.

### Ingerss:
1. Ingress
   helm install ingress ./ingress


### Monitoring
   1. kubectl create namespace monitoring 
   2. helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   3. helm repo add stable https://charts.helm.sh/stable
   4. helm repo update
   5. helm install prom prometheus-community/kube-prometheus-stack -f ./monitoring/prometheus.yaml --atomic --namespace "monitoring"
   6. kubectl port-forward service/prom-grafana 9000:80 --namespace "monitoring"


Not working:
1. Keycloak 
   helm install keycloak ./idp/keycloak/




### Unistall all:
   helm uninstall prom
   helm uninstall ingress 
   helm uninstall org 
   helm uninstall keycloak 
   helm uninstall org-db 
   helm uninstall keycloakdb 
   helm uninstall home-rp
