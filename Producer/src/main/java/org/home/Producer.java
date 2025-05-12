package org.home;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

public class Producer {

    @CrossOrigin(origins = "http://localhost:5173")
    @RestController
    public static class ProducerController {
        private final KafkaTemplate<String, MessageJSON> kafkaTemplate;

        MessageJSON exploreResponse = new MessageJSON("Product Explored");
        MessageJSON buyResponse = new MessageJSON("Product Bought");

        public ProducerController(KafkaTemplate<String, MessageJSON> kafkaTemplate) {
            this.kafkaTemplate = kafkaTemplate;
        }

        @PostMapping("/event/explore")
        public void sendExploreNotification() {
            kafkaTemplate.send("exploreTopic", exploreResponse);
        }

        @PostMapping("/event/buy")
        public void sendBuyNotification() {
            kafkaTemplate.send("buyTopic", buyResponse);
        }
    }
}
