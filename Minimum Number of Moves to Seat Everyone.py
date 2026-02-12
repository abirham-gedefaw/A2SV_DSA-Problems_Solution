class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sorted_seat = sorted(seats)
        sorted_student = sorted(students)

        moves = 0
        for i in range(len(seats)):
            moves += abs(sorted_student[i] - sorted_seat[i])

        return moves
