# hrp



## k8s Deploy

Execute from deployment directory:
0. NameSpace
   helm install home-rp ./homerp-namespace

DB's:
1. Keycloak DB 
   helm install keycloakdb ./dbs/keycloakdb
2. OrgDB
   helm install org-db ./dbs/org_db

Services:
...

Not working:
2. Keycloak 
   helm install keycloak ./idp/keycloak/
