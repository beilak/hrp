# hrp



## k8s Deploy
Execute from deployment directory:

### 0. NameSpace
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
1. helm install ingress ./ingress

Not working:
1. Keycloak 
   helm install keycloak ./idp/keycloak/


### Unistall all:
   helm uninstall ingress org keycloak org-db keycloakdb
