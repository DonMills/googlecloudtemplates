gke.yaml - a single run configuration file to create a 2 node gke cluster

```gcloud deployment-manager deployments create testdeploygke --config gke.yaml --preview```

This deploys the cluster in preview mode.

```gcloud deployment-manager deployments update testdeploygke --config gke.yaml```

This actually deploys after the preview.

```gcloud container clusters describe drmtestcluster -z us-east1-b```

This describes the cluster for you. 

------------------
gkecluster.py - a python template version of the above

gketemp.yaml - a config file that uses the template and sets the variables

```gcloud container clusters describe drmtest -z us-east1-b | grep clusterCaCertificate```
