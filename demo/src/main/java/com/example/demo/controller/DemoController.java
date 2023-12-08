package com.example.demo.controller;




@RestController
public class DemoController {
    @Autowired
    VertrixService vertrixService;

    @GetMapping("/{id}")
    public ResponseEntity<MerchantName> getName(@PathVariable("name") String name) {
        //Product product = productService.getProduct(id);
        return ResponseEntity.ok(MerchantName);
    }
}
