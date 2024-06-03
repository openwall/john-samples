## Description

- Sample n°1 : 
    - username "rinternet"
    - radius shared-password "true"

- Sample n°2 : 
    - username "jtan"
    - radius shared-password "123456"

- Sample n°3 : 
    - username "John.McGuirk" 
    - supplicant password "S0cc3r"

- Sample n°4 : 
    - username "steve"
    - radius shared-password "testing123"
    - supplicant password "testing"
    - Description of packets: | Frame | Description | shared secret | | on server | on client | | 1-4 | user steve authenticating with EAP-MD5, password bad (Access rejected) | testing123 | | 5-8 | user steve authenticating with EAP-MD5, password testing (Access Accepted) | testing123 | | 9-10 | same user, same password, PAP (Access Accepted) | testing123 | | 11-12 | same user/password, CHAP (Access Accepted) | testing123 | | 13-14 | same user, password bad_passsword, PAP (Access Rejected) | testing123 | | 15-17 | The client has a wrong shared secret, the server does not answer | bad_secret | testing123 | | 18-19 | Authentication successfull with PAP | bad_secret |

- Sample n° 5 : 
    - username "bob"
    - radius shared-password "iNJ72r0uPXP5qhAX"
    - supplicant password "ThisIsThePassword"

## Origins of the samples

- Sample n°1 & Sample n°2 : Maxime GOYETTE https://github.com/openwall/john/pull/3621#issuecomment-458752330
- Sample °3 : https://packetlife.net/captures/protocol/radius/
- Sample n°4 : https://wiki.wireshark.org/SampleCaptures
- Sample n°5 : https://weberblog.net/radius-tacacs-pcap/