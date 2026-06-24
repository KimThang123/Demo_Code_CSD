"""
Module: product.py
Định nghĩa lớp Product đại diện cho một sản phẩm trong hệ thống.
Mỗi sản phẩm có các thuộc tính: id, tên, giá, đánh giá, thương hiệu, danh mục, khuyến mãi.
"""
#cac ham co ban cua du an 
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
    

    class SearchEngine:
    """
    Cung cấp chức năng tìm kiếm sản phẩm theo từ khóa.
    Thuật toán: Linear scan (duyệt tuần tự) - O(n) với n là số sản phẩm.
    Phù hợp với quy mô ≤500 sản phẩm.
    """
    def __init__(self, repository: ProductRepository):
        self.repo = repository

    def search_by_keyword(self, keyword: str) -> List[Product]:
        """
        Tìm kiếm sản phẩm có tên chứa keyword (không phân biệt hoa/thường).
        Thuật toán: Duyệt toàn bộ master list, kiểm tra contains.
        Độ phức tạp: O(n * L) với L là độ dài tên trung bình.
        Kết quả trả về: List[Product] các sản phẩm khớp, có thể rỗng.
        """
        if not keyword:
            # Nếu từ khóa rỗng, trả về toàn bộ danh sách
            return self.repo.get_all_products()
        keyword_lower = keyword.lower()
        result = []
        for product in self.repo.get_all_products():
            if keyword_lower in product.name.lower():
                result.append(product)
        return result
