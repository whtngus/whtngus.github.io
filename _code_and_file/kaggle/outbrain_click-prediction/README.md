# 데이터 설명

### page_views.csv
    ID : 사용자 식별자
    ad_id : 광고 식별자
    advertiser_id : 광고주 식별자
    campaign_id : 캠페인

### page_views.csv
    uuid
    document_id
    timestamp  : 1465876799998을 빼면 원래 시간
    platform  : desktop = 1, mobile = 2, tablet =3
    geo_location  : country>state>DMA
    traffic_source : internal = 1, search = 2, social = 3

### clicks_train.csv
        display_id
        ad_id
        clicked  :  1 클릭함, 0 클릭 안함
        
### events.csv
           display_id
           uuid
           document_id
           timestamp
           platform
           geo_location
         
### promoted_content.csv
        ad_id
        document_id
        campaign_id
        advertiser_id
        
### documents_meta.csv
> document 상세 정보 제공 <br>

        document_id
        source_id  : 사이트 url 정보인듯
        publisher_id
        publish_time