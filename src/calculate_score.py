# this fuction is to calculate student's engagement score


def calculate_engagement_score(
    total_attendance_lectures=0,
    total_attendance_lab=0,
    total_attendance_support=0,
    total_canvas_activity=0,
    total_lectures=33,
    total_labs=22,
    total_support_sessions=44,
    total_canvas_expected=55,
    weight_lecture=0.3,
    weight_lab=0.4,
    weight_support=0.15,
    weight_canvas=0.15,
):
    try:
        if total_attendance_lectures < 0:
            total_attendance_lectures = 0
        if total_attendance_lab < 0:
            total_attendance_lab = 0
        if total_attendance_support < 0:
            total_attendance_support = 0
        if total_canvas_activity < 0:
            total_canvas_activity = 0
    
        student_engagement_score = (
            (total_attendance_lectures * weight_lecture / total_lectures)
            + (total_attendance_lab * weight_lab / total_labs)
            + (total_attendance_support * weight_support / total_support_sessions)
            + (total_canvas_activity * weight_canvas / total_canvas_expected)
        )
        return f'{student_engagement_score * 100:.2f}'
    except Exception as e:
        return f'Error: {e}'

