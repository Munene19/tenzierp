# Tenzierp

<a id="more_details"></a>

This app works to integrate ERPNext with KRA's eTIMS via the Online Sales Control Unit (OSCU) to allow for the sharing of information with the revenue authority.

This integration allows the user to send and receive the required information after sales, and purchase transactions, updating inventory, and creating customers. The user can also register their information such as items to the eTims servers.

For more details about eTims:

<a id="etims_official_documentation"></a>

https://www.kra.go.ke/images/publications/OSCU_Specification_Document_v2.0.pdf


## Summary of Integrated Endpoints

| Endpoint              |   Status   | [Documentation Section](#more_details) |
| :-------------------- | :--------: | -------------------------------------: |
| DeviceVerificationReq | Completely |                                3.3.1.1 |
| CodeSearchReq         | Completely |                                3.3.2.1 |
| CustSearchReq         | Completely |                                3.3.2.2 |
| NoticeSearchReq       | Completely |                                3.3.2.3 |
| ItemClsSearchReq      | Completely |                                3.3.3.1 |
| ItemSaveReq           | Completely |                                3.3.3.2 |
| ItemSearchReq         | Completely |                                3.3.3.3 |
| BhfSearchReq          | Completely |                                3.3.4.1 |
| BhfCustSaveReq        | Completely |                                3.3.4.2 |
| BhfUserSaveReq        | Completely |                                3.3.4.3 |
| BhfInsuranceSaveReq   | Completely |                                3.3.4.4 |
| ImportItemSearchReq   | Completely |                                3.3.5.1 |
| ImportItemUpdateReq   | Completely |                                3.3.5.2 |
| TrnsSalesSaveWrReq    | Completely |                                3.3.6.1 |
| TrnsPurchaseSalesReq  | Completely |                                3.3.7.1 |
| TrnsPurchaseSaveReq   | Completely |                                3.3.7.2 |
| StockMoveReq          | Completely |                                3.3.8.1 |
| StockIOSaveReq        | Completely |                                3.3.8.2 |
| StockMasterSaveReq    | Completely |                                3.3.8.2 |
| SaveItemComposition   | Completely | Section not specified in documentation |