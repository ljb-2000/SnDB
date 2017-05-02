HOST_TOTAL_DATA = "select a.id as id, a.name as name, a.cpu as cpu, a.memory as memory, a.disk as disk, group_concat(distinct b.ip separator ' ') as private_ip, group_concat(distinct c.ip separator ' ') as publish_ip, group_concat(distinct d.ip separator ' ') as vip_ip, a.host_ip as host_ip, e.name as idc, f.name as host_type, g.name as system, h.name as env, a.status as status, a.comment as comment, k.name as business, group_concat(distinct m.name separator ' ') as service, a.owner as owner from hosts a left join private_ips b on a.id = b.host_id left join publish_ips c on a.id = c.host_id left join host_vip_ip x on x.host_id = a.id left join vip_ips d on x.vip_ip_id = d.id left join idcs e on a.idc_id = e.id left join host_types f on a.host_type_id = f.id left join systems g on a.system_id = g.id left join envs h on a.env_id = h.id left join businesses k on a.business_id = k.id left join service_host n on n.host_id = a.id left join services m on m.id = n.service_id group by a.id;"


HOST_BUSINESS_DATA = "select a.id as id, a.name as name, a.cpu as cpu, a.memory as memory, a.disk as disk, group_concat(distinct b.ip separator ' ') as private_ip, group_concat(distinct c.ip separator ' ') as publish_ip, group_concat(distinct d.ip separator ' ') as vip_ip, a.host_ip as host_ip, e.name as idc, f.name as host_type, g.name as system, h.name as env, a.status as status, a.comment as comment, k.name as business, group_concat(distinct m.name separator ' ') as service, a.owner as owner from hosts a left join private_ips b on a.id = b.host_id left join publish_ips c on a.id = c.host_id left join host_vip_ip x on x.host_id = a.id left join vip_ips d on x.vip_ip_id = d.id left join idcs e on a.idc_id = e.id left join host_types f on a.host_type_id = f.id left join systems g on a.system_id = g.id left join envs h on a.env_id = h.id left join businesses k on a.business_id = k.id left join service_host n on n.host_id = a.id left join services m on m.id = n.service_id where k.id = {} group by a.id;"


APP_TOTAL_DATA = "select a.id as id, a.name as name, a.name_alias as name_alias, a.port as port, b.name as business, c.name as priority, d.name as user, a.contact as contact, a.contact_email as contact_email, a.status as status, a.comment as comment, a.db_instance as db_instance, group_concat(distinct e.ip separator ' ') as private_ip, group_concat(distinct f.ip separator ' ') as publish_ip, group_concat(distinct g.name separator ' ') as depend, group_concat(distinct h.name separator ' ') as domain from services a left join businesses b on a.business_id = b.id left join priorities c on a.priority_id = c.id left join serviceusers d on a.user_id = d.id left join service_private_ip e1 on a.id = e1.service_id left join private_ips e on e.id = e1.private_ip_id left join service_publish_ip f1 on a.id = f1.service_id left join publish_ips f on f.id = f1.publish_ip_id left join service_depend g1 on a.id = g1.service_id left join depends g on g.id = g1.depend_id left join service_domain h1 on a.id = h1.service_id left join domains h on h.id = h1.domain_id group by a.id;"


IDC_ID_DATA = "select a.id as id, a.name as name, a.cpu as cpu, a.memory as memory, a.disk as disk, group_concat(distinct b.ip separator ' ') as private_ip, group_concat(distinct c.ip separator ' ') as publish_ip, group_concat(distinct d.ip separator ' ') as vip_ip, a.host_ip as host_ip, e.name as idc, f.name as host_type, g.name as system, h.name as env, a.status as status, a.comment as comment, k.name as business, group_concat(distinct m.name separator ' ') as service, a.owner as owner from hosts a left join private_ips b on a.id = b.host_id left join publish_ips c on a.id = c.host_id left join host_vip_ip x on a.id = x.host_id left join vip_ips d on x.vip_ip_id = d.id left join idcs e on a.idc_id = e.id left join host_types f on a.host_type_id = f.id left join systems g on a.system_id = g.id left join envs h on a.env_id = h.id left join businesses k on a.business_id = k.id left join service_host n on n.host_id = a.id left join services m on m.id = n.service_id where e.id = {} group by a.id;"


HOST_ID_DATA = "select a.id as id, a.name as name, a.cpu as cpu, a.memory as memory, a.disk as disk, group_concat(distinct b.ip separator ' ') as private_ip, group_concat(distinct c.ip separator ' ') as publish_ip, group_concat(distinct d.ip separator ' ') as vip_ip, a.host_ip as host_ip, e.name as idc, f.name as host_type, g.name as system, h.name as env, a.status as status, a.comment as comment, k.name as business, group_concat(distinct m.name separator ' ') as service, a.owner as owner from hosts a left join private_ips b on a.id = b.host_id left join publish_ips c on a.id = c.host_id left join host_vip_ip x on a.id = x.host_id left join vip_ips d on x.vip_ip_id = d.id left join idcs e on a.idc_id = e.id left join host_types f on a.host_type_id = f.id left join systems g on a.system_id = g.id left join envs h on a.env_id = h.id left join businesses k on a.business_id = k.id left join service_host n on n.host_id = a.id left join services m on m.id = n.service_id where k.id = {} and e.id = {} group by a.id;"


COMPANY_ID_DATA = "select a.id as id, a.name as name, a.name_alias as name_alias, a.port as port, b.name as business, c.name as priority, d.name as user, a.contact as contact, a.contact_email as contact_email, a.status as status, a.comment as comment, a.db_instance as db_instance, group_concat(distinct e.ip separator ' ') as private_ip, group_concat(distinct f.ip separator ' ') as publish_ip, group_concat(distinct g.name separator ' ') as depend, group_concat(distinct h.name separator ' ') as domain from services a left join businesses b on a.business_id = b.id left join priorities c on a.priority_id = c.id left join serviceusers d on a.user_id = d.id left join service_private_ip e1 on a.id = e1.service_id left join private_ips e on e.id = e1.private_ip_id left join service_publish_ip f1 on a.id = f1.service_id left join publish_ips f on f.id = f1.publish_ip_id left join service_depend g1 on a.id = g1.service_id left join depends g on g.id = g1.depend_id left join service_domain h1 on a.id = h1.service_id left join domains h on h.id = h1.domain_id where instr(b.product, {}) group by a.id;"


BUSINESS_ID_DATA = "select a.id as id, a.name as name, a.name_alias as name_alias, a.port as port, b.name as business, c.name as priority, d.name as user, a.contact as contact, a.contact_email as contact_email, a.status as status, a.comment as comment, a.db_instance as db_instance, group_concat(distinct e.ip separator ' ') as private_ip, group_concat(distinct f.ip separator ' ') as publish_ip, group_concat(distinct g.name separator ' ') as depend, group_concat(distinct h.name separator ' ') as domain from services a left join businesses b on a.business_id = b.id left join priorities c on a.priority_id = c.id left join serviceusers d on a.user_id = d.id left join service_private_ip e1 on a.id = e1.service_id left join private_ips e on e.id = e1.private_ip_id left join service_publish_ip f1 on a.id = f1.service_id left join publish_ips f on f.id = f1.publish_ip_id left join service_depend g1 on a.id = g1.service_id left join depends g on g.id = g1.depend_id left join service_domain h1 on a.id = h1.service_id left join domains h on h.id = h1.domain_id where b.id = {} group by a.id;"


APP_COMPANY_TOTAL_DATA = "select a.id as id, a.name as name, a.name_alias as name_alias, a.port as port, b.name as business, c.name as priority, d.name as user, a.contact as contact, a.contact_email as contact_email, a.status as status, a.comment as comment, a.db_instance as db_instance, group_concat(distinct e.ip separator ' ') as private_ip, group_concat(distinct f.ip separator ' ') as publish_ip, group_concat(distinct g.name separator ' ') as depend, group_concat(distinct h.name separator ' ') as domain from services a left join businesses b on a.business_id = b.id left join priorities c on a.priority_id = c.id left join serviceusers d on a.user_id = d.id left join service_private_ip e1 on a.id = e1.service_id left join private_ips e on e.id = e1.private_ip_id left join service_publish_ip f1 on a.id = f1.service_id left join publish_ips f on f.id = f1.publish_ip_id left join service_depend g1 on a.id = g1.service_id left join depends g on g.id = g1.depend_id left join service_domain h1 on a.id = h1.service_id left join domains h on h.id = h1.domain_id group by a.id;"


CHOICE_HOST_TYPE_DATA = "select a.id from hosts a join host_types b on a.host_type_id = b.id and b.name = '物理机';"


BUSINESS_SERVICE_HOST_DATA = "select a.name, count(distinct b.id) as service, group_concat(distinct d.id) as host from businesses a join services b on b.business_id = a.id join service_host c on c.service_id = b.id join hosts d on d.id = c.host_id where a.id = {} group by a.name;"


IDC_SERVICE_HOST_TYPE_DATA = "select a.name as name, count(distinct d.id) as service, w.type from idcs a join hosts b on b.idc_id = a.id join service_host c on c.host_id = b.id join services d on d.id = c.service_id join (select f.name as name, group_concat(concat(f.type, ':', f.count)) as type from (select a.name as name, c.name as type, count(*) as count from idcs a join hosts b on b.idc_id = a.id join host_types c on c.id = b.host_type_id group by a.name, c.name) f group by f.name) w on w.name = a.name group by a.name;"


SERVICE_IP_DATA = "select a.id as service_id, a.name as name, a.name_alias as name_alias, a.port as port, f.id as business_id, f.name as business, g.id as priority_id, g.name as priority, h.id as user_id, h.name as user, a.contact as contact, a.contact_email as contact_email, a.comment as comment, a.db_instance as db_instance, a.status as status, group_concat(distinct c.ip) as private_ip, ifnull(group_concat(distinct e.ip), '') as publish_ip, ifnull(group_concat(distinct j.name), '') as depend, ifnull(group_concat(distinct k.name), '') as domain from services a left join service_private_ip b on b.service_id = a.id left join private_ips c on c.id = b.private_ip_id left join service_publish_ip d on d.service_id = a.id left join publish_ips e on e.id = d.publish_ip_id left join businesses f on f.id = a.business_id left join priorities g on g.id = a.priority_id left join serviceusers h on h.id = a.user_id left join service_domain m on m.service_id = a.id left join domains k on k.id = m.domain_id left join service_depend n on n.service_id = a.id left join depends j on j.id = n.depend_id where c.ip = '{}' group by a.name;"


BUSINESS_HOST_IDC_DATA = "select a.name as name, ifnull(group_concat(distinct c.ip), '') as private_ip from idcs a left join hosts b on b.idc_id = a.id left join private_ips c on c.host_id = b.id left join businesses d on d.id = b.business_id where d.id = '{}' group by a.name;"


HOST_IDC_SERVICE_BUSINESS_DATA = "select a.name as name, a.cpu as cpu, a.memory as memory, a.disk as disk, ifnull(group_concat(distinct b.ip separator ' '), '') as private_ip, ifnull(group_concat(distinct c.ip separator ' '), '') as publish_ip, ifnull(group_concat(distinct d.ip separator ' '), '') as vip_ip, a.host_ip as host_ip, e.name as idc, f.name as host_type, g.name as system, h.name as env, k.name as business, ifnull(group_concat(distinct m.name separator ' '), '') as service, a.owner as owner, a.comment as comment from hosts a left join private_ips b on a.id = b.host_id left join publish_ips c on a.id = c.host_id left join host_vip_ip x on x.host_id = a.id left join vip_ips d on x.vip_ip_id = d.id left join idcs e on a.idc_id = e.id left join host_types f on a.host_type_id = f.id left join systems g on a.system_id = g.id left join envs h on a.env_id = h.id left join businesses k on a.business_id = k.id left join service_host n on n.host_id = a.id left join services m on m.id = n.service_id group by a.id;"
