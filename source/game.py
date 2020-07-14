

def has_collision_between(source, target):
    """
    Helper function to check the overlap between rectangular areas.
    """
    return (
        source.y >= target.y - target.height and
        source.y - source.height <= target.y and
        source.x + source.width >= target.x and
        source.x <= target.x + target.width
    )

