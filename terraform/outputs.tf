output "cluster_name" {
  value = module.aks_cluster.cluster_name
}

output "cluster_id" {
  value = module.aks_cluster.cluster_id
}

output "kube_config" {
  value     = module.aks_cluster.kube_config
  sensitive = true
}
