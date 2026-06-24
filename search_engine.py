
class SearchEngine:
    """
    Cung cấp chức năng tìm kiếm sản phẩm theo từ khóa.
    Thuật toán: Linear scan (duyệt tuần tự) - O(n) với n là số sản ph
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