Sanitized out = datastor {
    low water mark 80
    high water mark 90
}
deduplication {}
packet filter foo-bar-123456 {
    order 2
    action accept
    filter { ( src host 10.100.102.103 ) and ( dst net 172.100.200.0/24 ) }
}
pool test-pool {
    monitor all http-conn-close
    members {
        172.100.200.32%1:http {}
        172.100.200.223%1:http {}
    }
}
