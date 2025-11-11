from paddleocr import PaddleOCR

img_path = r"D:\gemini-paddle-api\picture\thai_id_card_front_bunyang.png"


def paddle_ocr(img_path):

    ocr = PaddleOCR(
        lang="th",
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )

    # Run OCR inference on a sample image
    result = ocr.predict(input=img_path)

    # Visualize the results and save the JSON results
    for res in result:
        # coor = res["rec_boxes"]
        res.print()
        res.save_to_img("output")
        res.save_to_json("output")


if __name__ == "__main__":
    paddle_ocr(img_path)
