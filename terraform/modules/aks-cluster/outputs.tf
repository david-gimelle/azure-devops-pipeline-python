output "cluster_name" {
  value = azurerm_kubernetes_cluster.main.name
}

output "cluster_id" {
  value = azurerm_kubernetes_cluster.main.id
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.main.kube_config_raw
}

output "host" {
  value = azurerm_kubernetes_cluster.main.kube_config[0].host
}

output "client_certificate" {
  value = azurerm_kubernetes_cluster.main.kube_config[0].client_certificate
}
