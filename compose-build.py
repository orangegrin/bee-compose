#!/usr/bin/python
import sys
head='''version: "3"

services:'''
clef='''
  clef-%s:
    image: ethersphere/clef:0.4.12
    restart: unless-stopped
    environment:
      - CLEF_CHAINID
    volumes:
      - clef-%s:/app/data
    command: full'''
bee='''
  bee-%s:
    image: ethersphere/bee:beta
    restart: unless-stopped
    environment:
      - BEE_API_ADDR
      - BEE_BLOCK_TIME
      - BEE_BOOTNODE
      - BEE_BOOTNODE_MODE
      - BEE_CLEF_SIGNER_ENABLE
      - BEE_CLEF_SIGNER_ENDPOINT=http://clef-%s:8550
      - BEE_CONFIG
      - BEE_CORS_ALLOWED_ORIGINS
      - BEE_DATA_DIR
      - BEE_CACHE_CAPACITY
      - BEE_DB_OPEN_FILES_LIMIT
      - BEE_DB_BLOCK_CACHE_CAPACITY
      - BEE_DB_WRITE_BUFFER_SIZE
      - BEE_DB_DISABLE_SEEKS_COMPACTION
      - BEE_DEBUG_API_ADDR
      - BEE_DEBUG_API_ENABLE
      - BEE_GATEWAY_MODE
      - BEE_GLOBAL_PINNING_ENABLE
      - BEE_FULL_NODE
      - BEE_NAT_ADDR
      - BEE_NETWORK_ID
      - BEE_P2P_ADDR
      - BEE_P2P_QUIC_ENABLE
      - BEE_P2P_WS_ENABLE
      - BEE_PASSWORD
      - BEE_PASSWORD_FILE
      - BEE_PAYMENT_EARLY
      - BEE_PAYMENT_THRESHOLD
      - BEE_PAYMENT_TOLERANCE
      - BEE_POSTAGE_STAMP_ADDRESS
      - BEE_RESOLVER_OPTIONS
      - BEE_STANDALONE
      - BEE_SWAP_ENABLE
      - BEE_SWAP_ENDPOINT
      - BEE_SWAP_FACTORY_ADDRESS
      - BEE_SWAP_LEGACY_FACTORY_ADDRESSES
      - BEE_SWAP_INITIAL_DEPOSIT
      - BEE_SWAP_DEPLOYMENT_GAS_PRICE
      - BEE_TRACING_ENABLE
      - BEE_TRACING_ENDPOINT
      - BEE_TRACING_SERVICE_NAME
      - BEE_TRANSACTION
      - BEE_VERBOSITY
      - BEE_WELCOME_MESSAGE
    ports:
      - "${API_ADDR:-%s}${BEE_API_ADDR:-:1633}"
      - "${P2P_ADDR:-%s}${BEE_P2P_ADDR:-:1634}"
      - "${DEBUG_API_ADDR:-:%s}${BEE_DEBUG_API_ADDR:-:1635}"
    volumes:
      - bee-%s:/home/bee/.bee
    command: start
    depends_on:
      - clef-%s
'''

volumetage='''
volumes:'''
volumes='''
  clef-%s:
  bee-%s:'''
text=''
def flow():    
    fo = open("docker-compose.yml", "w")
    fo.write(text)
    fo.close()
    print("flow")


def create(count):
    api_port=1000
    p2p_port=1500
    debug_port=2000
    global text
    text +=head
    # services
    for i in range(1,count+1):
        api_port+=1
        p2p_port+=1
        debug_port+=1
        text+=clef%(i,i)
        text+=bee%(i,i,api_port,p2p_port,debug_port,i,i)
    #volumes
    text +=volumetage
    for i in range(1,count+1):
        text+=volumes%(i,i)
try:
  count=sys.argv[1]
except:
  count = input("启动数量：")
create(int(count))
flow()