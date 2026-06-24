"""
Module: product.py
Định nghĩa lớp Product đại diện cho một sản phẩm trong hệ thống.
Mỗi sản phẩm có các thuộc tính: id, tên, giá, đánh giá, thương hiệu, danh mục, khuyến mãi.
"""

class Product:
    """
    Lớp Product biểu diễn một sản phẩm trong catalog thương mại điện tử.
    """
    def __init__(self, id: int, name: str, price: float, rating: int, brand: str, category: str):
        """
        Khởi tạo một sản phẩm mới.
        """
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating
        self.brand = brand
        self.category = category
    def __repr__(self) -> str:
        """Trả về chuỗi biểu diễn sản phẩm, theo format bất kì"""
        return (f"Product(id={self.id}, name='{self.name}', price={self.price}, "
                f"rating={self.rating}, brand='{self.brand}', category='{self.category}', "
                f"promotion={self.has_promotion})")

    def __str__(self) -> str:
        """Trả về chuỗi hiển thị thân thiện với người dùng."""
        return f"{self.name} - {self.price} VND - {self.rating}sss - {self.brand} - {self.category}"