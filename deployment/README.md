## Deploy

Execute from deployment:
0. NameSpace
   helm install home-rp ./homerp-namespace
1. Keycloak DB 
   helm install keycloakdb ./dbs/keycloakdb
2. Keycloak 
   helm install keycloak ./idp/keycloak/