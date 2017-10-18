##############################################3
### creates a gke cluster
### DRM 10/18/17
################################################

def GenerateConfig(context):
	"""Generate Configuration."""
	resources = []
        resources.append({
		'name': 'gke-' + context.env['deployment'],
		'type': 'container.v1.cluster',
		'properties' : {
			'zone': context.properties['zone'],
			'cluster': {
     				'name': context.properties['clustername'],
     				'description': context.properties['clusterdesc'],
    				'nodePools': [{
     					'name': context.properties['clustername'] + "-" + context.properties['zone'],
       					'config': {
         					'machineType': 'n1-standard-1',
         					'diskSizeGb': 100,
         					'oauthScopes': ["https://www.googleapis.com/auth/devstorage.read_only"],
         					'imageType': 'cos',
         					'preemptible': context.properties['preemptible']
						},
       					'initialNodeCount': context.properties['initialcount'],
       					'management': {
         					'autoUpgrade': True,
  						'autoRepair': True
							}
					
				}],
     			'masterAuth': {
       				'username': context.properties['username'],
       				'password': context.properties['password']
				}
			}
		}
	})
	return {'resources': resources}	
