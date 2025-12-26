#24331A05D8
#Program to assign question paper sets to students on different cases.
import random
# ============================================================================
# 1. FLEXIBLE ROLL NUMBER GENERATION SYSTEM
# ============================================================================

def parse_roll_number(roll_num_str):
    """Parses roll number to extract character and numeric parts."""
    roll_num_str = roll_num_str.strip()
    i = len(roll_num_str) - 1

    while i >= 0 and roll_num_str[i].isdigit():
        i -= 1

    if i < len(roll_num_str) - 1:
        num_part = int(roll_num_str[i+1:])
        prefix_and_char = roll_num_str[:i+1]
    else:
        num_part = None
        prefix_and_char = roll_num_str

    return prefix_and_char, num_part


def generate_roll_number_range(start_roll, end_roll, prefix=""):
    """Generates roll numbers from start to end."""
    roll_numbers = []

    start_prefix, start_num = parse_roll_number(start_roll)
    end_prefix, end_num = parse_roll_number(end_roll)

    if start_prefix == "" and end_prefix == "" and start_num is not None and end_num is not None:
        for num in range(start_num, end_num + 1):
            roll_numbers.append(f"{prefix}{num}")
        return roll_numbers

    start_char = start_prefix.replace(prefix, "")
    end_char = end_prefix.replace(prefix, "")

    if len(start_char) == 1 and len(end_char) == 1 and start_char.isalpha() and end_char.isalpha():
        for char_code in range(ord(start_char.lower()), ord(end_char.lower()) + 1):
            char = chr(char_code)

            if char == start_char.lower():
                digit_start = start_num if start_num is not None else 0
            else:
                digit_start = 0

            if char == end_char.lower():
                digit_end = end_num if end_num is not None else 9
            else:
                digit_end = 9

            for digit in range(digit_start, digit_end + 1):
                roll_numbers.append(f"{prefix}{char}{digit}")

    elif start_char == end_char and start_num is not None and end_num is not None:
        for num in range(start_num, end_num + 1):
            roll_numbers.append(f"{prefix}{start_char}{num}")

    else:
        raise ValueError(f"Unable to parse range from '{start_roll}' to '{end_roll}'")

    return roll_numbers


def generate_default_roll_numbers():
    """Generates the default roll numbers."""
    print("\nUsing default configuration: 24331A05d3-j8 and LE13-LE19")
    roll_numbers = []
    prefix = "24331A05"

    for char_code in range(ord('d'), ord('k')):
        char = chr(char_code)
        start_digit = 3 if char == 'd' else 0
        end_digit = 9 if char != 'j' else 8

        for digit in range(start_digit, end_digit + 1):
            roll_numbers.append(f"{prefix}{char}{digit}")

    for digit in range(13, 20):
        roll_numbers.append(f"LE{digit}")

    return roll_numbers


def get_lateral_entries_from_user():
    """Collects lateral entry roll numbers."""
    print("\n" + "="*70)
    print(" LATERAL ENTRY STUDENTS")
    print("="*70)

    lateral_entries = []

    has_lateral = input("\nDo you have any lateral entry students? (Y/N): ").strip().upper()

    if has_lateral != 'Y':
        print("No lateral entry students.")
        return lateral_entries

    print("\nHow would you like to enter lateral entry roll numbers?")
    print("  1. Enter a range (e.g., LE13 to LE19)")
    print("  2. Enter individual roll numbers manually")

    while True:
        le_choice = input("\nChoice (1 or 2): ").strip()

        if le_choice == '1':
            print("\nEnter lateral entry range:")
            start_le = input("  Start (e.g., LE13): ").strip()
            end_le = input("  End (e.g., LE19): ").strip()

            try:
                le_rolls = generate_roll_number_range(start_le, end_le, prefix="")
                lateral_entries.extend(le_rolls)
                print(f"  ✓ Added {len(le_rolls)} lateral entry students")
                print(f"  Range: {le_rolls[0]} to {le_rolls[-1]}")
            except Exception as e:
                print(f"  ❌ Error: {e}")
                print("  Lateral entries not added. Try again.")
                continue
            break

        elif le_choice == '2':
            print("\nEnter lateral entry roll numbers one by one.")
            print("Type 'DONE' when finished.\n")

            count = 1
            while True:
                le_roll = input(f"Lateral Entry {count} (or 'DONE'): ").strip()

                if le_roll.upper() == 'DONE':
                    break

                if le_roll:
                    lateral_entries.append(le_roll)
                    print(f"  ✓ Added: {le_roll}")
                    count += 1

            if lateral_entries:
                print(f"\n✓ Total lateral entry students: {len(lateral_entries)}")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

    if lateral_entries:
        add_more = input("\nAdd more lateral entry students? (Y/N): ").strip().upper()
        if add_more == 'Y':
            print("\nEnter additional lateral entry roll numbers.")
            print("Type 'DONE' when finished.\n")

            count = len(lateral_entries) + 1
            while True:
                le_roll = input(f"Lateral Entry {count} (or 'DONE'): ").strip()

                if le_roll.upper() == 'DONE':
                    break

                if le_roll:
                    lateral_entries.append(le_roll)
                    print(f"  ✓ Added: {le_roll}")
                    count += 1

    if lateral_entries:
        print(f"\n{'='*70}")
        print(f"LATERAL ENTRY SUMMARY: {len(lateral_entries)} students")
        print(f"{'='*70}")
        if len(lateral_entries) <= 15:
            for le in lateral_entries:
                print(f"  • {le}")
        else:
            print(f"  First 5: {', '.join(lateral_entries[:5])}")
            print(f"  Last 5: {', '.join(lateral_entries[-5:])}")

    return lateral_entries


# ============================================================================
# SIMPLIFIED ROLL NUMBER CONFIGURATION
# ============================================================================

def quick_roll_number_setup():
    """Quick and simple roll number setup for most common cases."""
    print("\n" + "="*70)
    print(" QUICK SETUP")
    print("="*70)

    print("\nEnter the common prefix (e.g., '24331A05')")
    prefix = input("Prefix (press Enter if none): ").strip()

    all_roll_numbers = []

    print("\nEnter the roll number range:")
    print("Examples: 'd3' to 'j8', '1' to '100', 'A0' to 'B7'")

    start = input("\nStart: ").strip()
    end = input("End: ").strip()

    try:
        roll_numbers = generate_roll_number_range(start, end, prefix)
        all_roll_numbers.extend(roll_numbers)
        print(f"\n✓ Generated {len(roll_numbers)} roll numbers")
        print(f"  From: {roll_numbers[0]}")
        print(f"  To: {roll_numbers[-1]}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Starting over...")
        return quick_roll_number_setup()

    has_lateral = input("\nAdd lateral entry students? (Y/N): ").strip().upper()

    if has_lateral == 'Y':
        print("\nLateral Entry Range:")
        le_start = input("Start (e.g., LE13): ").strip()
        le_end = input("End (e.g., LE19): ").strip()

        try:
            lateral_rolls = generate_roll_number_range(le_start, le_end, prefix="")
            all_roll_numbers.extend(lateral_rolls)
            print(f"✓ Added {len(lateral_rolls)} lateral entry students")
        except Exception as e:
            print(f"❌ Error with lateral entries: {e}")
            print("Skipping lateral entries.")

    print(f"\n{'='*70}")
    print(f"TOTAL: {len(all_roll_numbers)} roll numbers configured")
    print(f"{'='*70}")

    if len(all_roll_numbers) <= 15:
        print("\nAll roll numbers:")
        for rn in all_roll_numbers:
            print(f"  • {rn}")
    else:
        print("\nPreview:")
        print(f"  First 5: {', '.join(all_roll_numbers[:5])}")
        print(f"  Last 5: {', '.join(all_roll_numbers[-5:])}")

    confirm = input("\nProceed with these roll numbers? (Y/N): ").strip().upper()

    if confirm == 'Y':
        return all_roll_numbers
    else:
        print("\nRestarting configuration...")
        return quick_roll_number_setup()


def advanced_roll_number_setup():
    """Advanced setup with multiple ranges and full control."""
    print("\n" + "="*70)
    print(" ADVANCED SETUP")
    print("="*70)

    print("\nEnter the common prefix for REGULAR roll numbers (leave empty if none).")
    prefix = input("Prefix: ").strip()

    all_roll_numbers = []

    print("\nNow enter the REGULAR roll number ranges.")
    print("You can add multiple ranges. Type 'DONE' when finished.")

    range_count = 1
    while True:
        print(f"\n--- Regular Range {range_count} ---")
        start = input(f"Start (or 'DONE' to finish): ").strip()

        if start.upper() == 'DONE':
            break

        end = input(f"End: ").strip()

        try:
            range_rolls = generate_roll_number_range(start, end, prefix)
            all_roll_numbers.extend(range_rolls)
            print(f"  ✓ Added {len(range_rolls)} roll numbers")
            print(f"  Sample: {range_rolls[0]} ... {range_rolls[-1]}")
            range_count += 1
        except Exception as e:
            print(f"  ❌ Error: {e}")

    if not all_roll_numbers:
        print("\n⚠ No regular roll numbers configured.")
    else:
        print(f"\n✓ Total REGULAR roll numbers: {len(all_roll_numbers)}")

    lateral_entries = get_lateral_entries_from_user()
    all_roll_numbers.extend(lateral_entries)

    if not all_roll_numbers:
        print("\n❌ No roll numbers configured. Using default.")
        return generate_default_roll_numbers()

    print(f"\n{'='*70}")
    print(f"TOTAL: {len(all_roll_numbers)} roll numbers")
    print(f"  Regular: {len(all_roll_numbers) - len(lateral_entries)}")
    print(f"  Lateral Entry: {len(lateral_entries)}")
    print(f"{'='*70}")

    confirm = input("\nProceed? (Y/N): ").strip().upper()

    if confirm == 'Y':
        return all_roll_numbers
    else:
        return advanced_roll_number_setup()


def get_roll_numbers_simplified():
    """Simplified roll number configuration with 3 options."""
    print("\n" + "="*70)
    print(" ROLL NUMBER CONFIGURATION")
    print("="*70)

    print("\nHow would you like to configure roll numbers?")
    print("  1. Use default setup (24331A05d3-j8 and LE13-LE19)")
    print("  2. Quick setup (Enter prefix and simple range)")
    print("  3. Advanced setup (Custom ranges + lateral entries)")

    while True:
        choice = input("\nChoice (1, 2, or 3): ").strip()

        if choice == '1':
            return generate_default_roll_numbers()
        elif choice == '2':
            return quick_roll_number_setup()
        elif choice == '3':
            return advanced_roll_number_setup()
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


# ============================================================================
# 2. PENALTY CONFIGURATION (INCLUDES LATE COMER PENALTY)
# ============================================================================

def get_penalty_config_from_user():
    """Enhanced penalty configuration including late comers."""
    print("\n" + "="*70)
    print(" PENALTY CONFIGURATION")
    print("="*70)

    print("\nConfigure penalties for different scenarios.\n")

    # Retake penalties
    print("--- RETAKE PENALTIES ---")
    print("Students can retake the exam up to 2 times.")

    while True:
        try:
            penalty_1st = input("Marks penalty for 1st retake (e.g., 5): ").strip()
            penalty_1st = float(penalty_1st) if penalty_1st else 0

            penalty_2nd = input("Marks penalty for 2nd retake (e.g., 10): ").strip()
            penalty_2nd = float(penalty_2nd) if penalty_2nd else 0

            # Late comer penalty
            print("\n--- LATE COMER PENALTY ---")
            penalty_late = input("Marks penalty for late comers (e.g., 3, or 0 for none): ").strip()
            penalty_late = float(penalty_late) if penalty_late else 0

            print(f"\n✓ Penalty Configuration:")
            print(f"  1st Retake: -{penalty_1st} marks")
            print(f"  2nd Retake: -{penalty_2nd} marks")
            print(f"  Late Arrival: -{penalty_late} marks")

            confirm = input("\nConfirm these penalties? (Y/N): ").strip().upper()
            if confirm == 'Y':
                return {
                    'first_retake': penalty_1st,
                    'second_retake': penalty_2nd,
                    'late_comer': penalty_late
                }
            else:
                print("\nLet's reconfigure the penalties...\n")
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.\n")


# ============================================================================
# 3. TRACKER INITIALIZATION (INCLUDES LATE COMER FIELD)
# ============================================================================

def initialize_exam_tracker_enhanced(roll_numbers):
    """Enhanced tracker with retake, late comer, and penalty tracking."""
    tracker = {
        roll_num: {
            "present": False,
            "set_number": None,
            "retake_count": 0,
            "assigned": False,
            "retake_history": [],
            "marks_penalty": 0.0,
            "late_comer": False
        }
        for roll_num in roll_numbers
    }
    return tracker


# ============================================================================
# 4. IMPROVED SET ASSIGNMENT LOGIC
# ============================================================================

def get_next_set_improved(set_counts):
    """
    Improved set distribution with better randomness and spacing.

    Rules:
    1. No set can repeat within the last 4 assignments (minimum spacing)
    2. Prioritize sets that haven't been used recently
    3. True random selection from available sets
    """
    sets = list(range(1, 16))  # 15 Sets

    history = set_counts["history"]

    if len(history) < 4:
        # First 4 assignments - truly random
        next_set = random.choice(sets)
    else:
        # Look at last 4 assignments
        last_four = history[-4:]

        # Prohibited: Sets used in last 4 assignments
        prohibited_sets = set(last_four)

        # Available sets
        available_sets = [s for s in sets if s not in prohibited_sets]

        if not available_sets:
            # Fallback: If somehow all sets are prohibited, use any set
            available_sets = sets

        # SMART SELECTION: Prioritize less recently used sets
        if len(history) >= 10:
            # Count frequency of each set in last 10 assignments
            last_ten = history[-10:]
            frequency = {}
            for s in sets:
                frequency[s] = last_ten.count(s)

            # Find sets with lowest frequency in available sets
            min_freq = min(frequency[s] for s in available_sets)
            least_used = [s for s in available_sets if frequency[s] == min_freq]

            # Choose randomly from least used sets
            next_set = random.choice(least_used)
        else:
            # Random selection from available sets
            next_set = random.choice(available_sets)

    set_counts["history"].append(next_set)
    return next_set


# ============================================================================
# 5. DISTRIBUTION MODES
# ============================================================================

def distribute_by_sequence(roll_numbers, tracker, set_counts):
    """Mode 1: Teacher-led, sequential distribution."""
    print("\n--- Mode 1: Sequential Distribution ---")
    print("Enter attendance (1/0) or type 'STOP' to halt.")

    for roll_num in roll_numbers:
        if tracker[roll_num]["assigned"]:
            continue

        while True:
            try:
                status = input(f"Is student {roll_num} present? (1/0/STOP): ").upper()

                if status == 'STOP':
                    print("Assignment paused.")
                    return

                if status not in ('0', '1'):
                    raise ValueError

                tracker[roll_num]["assigned"] = True
                if status == '1':
                    set_num = get_next_set_improved(set_counts)
                    tracker[roll_num]["present"] = True
                    tracker[roll_num]["set_number"] = set_num
                    print(f"-> {roll_num} assigned SET {set_num}.")
                else:
                    tracker[roll_num]["present"] = False
                    print(f"-> {roll_num} marked Absent.")
                break
            except ValueError:
                print("Invalid input. Please enter '1', '0', or 'STOP'.")

    print("--- Sequential distribution complete. ---")


def distribute_by_roll_number(roll_numbers, tracker, set_counts):
    """Mode 2: Student-initiated roll number entry."""
    print("\n--- Mode 2: Roll Number Entry Distribution ---")
    print("Enter last two characters (e.g., 'd8', '19') or 'STOP' to halt/finish.")

    unassigned_suffixes = {r[-2:].upper(): r for r in roll_numbers if not tracker[r]["assigned"]}

    while unassigned_suffixes:
        print(f"\nRemaining students to assign: {len(unassigned_suffixes)}")
        suffix_input = input("Enter suffix or 'STOP': ").upper()

        if suffix_input in ('STOP', 'DONE'):
            print("Assignment paused/finished.")
            break

        if suffix_input in unassigned_suffixes:
            full_roll_num = unassigned_suffixes[suffix_input]

            set_num = get_next_set_improved(set_counts)
            tracker[full_roll_num]["present"] = True
            tracker[full_roll_num]["set_number"] = set_num
            tracker[full_roll_num]["assigned"] = True
            print(f"-> Roll number {full_roll_num} assigned SET {set_num}.")

            del unassigned_suffixes[suffix_input]

        elif any(r[-2:].upper() == suffix_input for r in roll_numbers):
            print(f"Error: Roll number suffix '{suffix_input}' is already processed.")
        else:
            print(f"Error: Invalid roll number suffix '{suffix_input}'.")

    for roll_num in list(unassigned_suffixes.values()):
        if not tracker[roll_num]["assigned"]:
            tracker[roll_num]["present"] = False
            tracker[roll_num]["assigned"] = True
            print(f"-> {roll_num} (unprocessed) marked Absent.")

    print("--- Roll number distribution complete. ---")


def distribute_fully_random(roll_numbers, tracker, set_counts):
    """Mode 3: Fully random order - assigns sets immediately when marking present."""
    print("\n--- Mode 3: Fully Random Distribution ---")
    print("Sets will be assigned immediately when you mark students present.")
    print("Enter attendance (1/0) or type 'STOP' to halt.")

    random_roll_order = list(roll_numbers)
    random.shuffle(random_roll_order)

    print("\n--- ATTENDANCE & SET ASSIGNMENT ---")

    for roll_num in random_roll_order:
        if tracker[roll_num]["assigned"]:
            continue

        while True:
            try:
                status = input(f"Is student {roll_num} present? (1/0/STOP): ").upper()

                if status == 'STOP':
                    print("Assignment paused.")
                    return

                if status not in ('0', '1'):
                    raise ValueError

                tracker[roll_num]["assigned"] = True

                if status == '1':
                    set_num = get_next_set_improved(set_counts)
                    tracker[roll_num]["present"] = True
                    tracker[roll_num]["set_number"] = set_num
                    print(f"-> {roll_num} assigned SET {set_num}.")
                else:
                    tracker[roll_num]["present"] = False
                    print(f"-> {roll_num} marked Absent.")
                break
            except ValueError:
                print("Invalid input. Please enter '1', '0', or 'STOP'.")

    print("--- Fully random distribution complete. ---")


# ============================================================================
# 6. LATE COMER HANDLING
# ============================================================================

def handle_late_comers(tracker, set_counts, penalty_config):
    """Handle late arriving students with optional penalty."""
    print("\n" + "="*70)
    print(" LATE COMERS")
    print("="*70)

    has_late = input("\nAre there any late comers? (Y/N): ").strip().upper()

    if has_late != 'Y':
        print("No late comers.")
        return

    print(f"\nLate comer penalty: -{penalty_config['late_comer']} marks")
    print("\nEnter late comer roll numbers. Type 'STOP' when done.\n")

    late_count = 0

    while True:
        late_input = input("Late comer roll number (or 'STOP'): ").strip()

        if late_input.upper() in ('STOP', 'DONE'):
            print(f"\nLate comer registration finished. Total: {late_count}")
            break

        late_input_upper = late_input.upper()

        # Try exact match first
        matching_rolls = [roll for roll in tracker.keys() 
                         if roll.upper() == late_input_upper]

        # Try suffix match if no exact match
        if not matching_rolls:
            matching_rolls = [roll for roll in tracker.keys() 
                             if roll.upper().endswith(late_input_upper)]

        if not matching_rolls:
            print(f"❌ Error: Roll number '{late_input}' not found.")
            continue

        if len(matching_rolls) > 1:
            print(f"❌ Error: Ambiguous input. Matches: {matching_rolls}")
            continue

        roll_num = matching_rolls[0]
        student_data = tracker[roll_num]

        # Check if already processed
        if student_data["assigned"] and student_data["present"]:
            print(f"❌ Error: {roll_num} was already marked present in main distribution.")
            print(f"   Current set: {student_data['set_number']}")
            continue

        # Assign set to late comer
        set_num = get_next_set_improved(set_counts)
        student_data["present"] = True
        student_data["set_number"] = set_num
        student_data["assigned"] = True
        student_data["late_comer"] = True
        student_data["marks_penalty"] += penalty_config['late_comer']

        print(f"✓ {roll_num} assigned SET {set_num}.")
        if penalty_config['late_comer'] > 0:
            print(f"   Late Penalty: -{penalty_config['late_comer']} marks")

        late_count += 1


# ============================================================================
# 7. RETAKE HANDLING WITH PENALTY
# ============================================================================

def handle_retakes_with_penalty(tracker, set_counts, penalty_config):
    """Enhanced retake handling with marks penalty (max 2 retakes)."""
    print("\n" + "="*70)
    print(" SET RETAKE OPTION")
    print("="*70)

    print(f"\nRetake Penalties:")
    print(f"  • 1st Retake: -{penalty_config['first_retake']} marks")
    print(f"  • 2nd Retake: -{penalty_config['second_retake']} marks")
    print(f"  • Maximum Retakes: 2")

    eligible_students = [
        roll for roll, data in tracker.items() 
        if data["present"] and data["set_number"] is not None and data["retake_count"] < 2
    ]

    if not eligible_students:
        print("\n⚠ No students eligible for retakes.")
        return

    print(f"\n✓ {len(eligible_students)} students eligible for retakes.\n")

    while True:
        retake_input = input("Enter roll number for retake (or 'STOP'): ").strip()

        if retake_input.upper() in ('STOP', 'DONE'):
            print("Retake session finished.")
            break

        retake_input_upper = retake_input.upper()

        matching_rolls = [roll for roll in tracker.keys() 
                         if roll.upper() == retake_input_upper]

        if not matching_rolls:
            matching_rolls = [roll for roll in tracker.keys() 
                             if roll.upper().endswith(retake_input_upper)]

        if not matching_rolls:
            print(f"❌ Error: Roll number '{retake_input}' not found.")
            continue

        if len(matching_rolls) > 1:
            print(f"❌ Error: Ambiguous input. Matches: {matching_rolls}")
            continue

        roll_num = matching_rolls[0]
        student_data = tracker[roll_num]

        if not student_data["present"]:
            print(f"❌ Error: {roll_num} was marked absent.")
        elif student_data["set_number"] is None:
            print(f"❌ Error: {roll_num} has no set assigned.")
        elif student_data["retake_count"] >= 2:
            print(f"❌ Error: {roll_num} has already used both retakes (max 2).")
        else:
            old_set = student_data["set_number"]
            new_set_num = get_next_set_improved(set_counts)

            student_data["retake_count"] += 1

            student_data["retake_history"].append({
                'old_set': old_set,
                'new_set': new_set_num,
                'retake_number': student_data["retake_count"]
            })

            if student_data["retake_count"] == 1:
                penalty = penalty_config['first_retake']
            else:
                penalty = penalty_config['second_retake']

            student_data["marks_penalty"] += penalty
            student_data["set_number"] = new_set_num

            print(f"✓ {roll_num}:")
            print(f"   Old Set: {old_set} → New Set: {new_set_num}")
            print(f"   Retake #{student_data['retake_count']} | Penalty: -{penalty} marks")
            print(f"   Total Penalty: -{student_data['marks_penalty']} marks")


# ============================================================================
# 8. REPORT GENERATION (WITH LATE COMER DETAILS)
# ============================================================================

def generate_report_enhanced(tracker, penalty_config):
    """Enhanced report with retake details, late comers, and marks penalty."""
    print("\n" + "="*70)
    print(" FINAL EXAM ASSIGNMENT REPORT")
    print("="*70)

    present_count = sum(1 for data in tracker.values() if data["present"])
    absent_count = sum(1 for data in tracker.values() if not data["present"] and data["assigned"])
    total_retakes = sum(data["retake_count"] for data in tracker.values())
    students_with_retakes = sum(1 for data in tracker.values() if data["retake_count"] > 0)
    late_comers_count = sum(1 for data in tracker.values() if data["late_comer"])

    set_counts = {}
    for data in tracker.values():
        if data["set_number"] is not None:
            set_counts[data["set_number"]] = set_counts.get(data["set_number"], 0) + 1

    print(f"\nTotal Students: {len(tracker)}")
    print(f"Students Present: {present_count}")
    print(f"Students Absent: {absent_count}")
    print(f"Total Retakes Taken: {total_retakes}")
    print(f"Students Who Retook: {students_with_retakes}")
    print(f"Late Comers: {late_comers_count}")

    print(f"\nPenalty Configuration:")
    print(f"  • 1st Retake: -{penalty_config['first_retake']} marks")
    print(f"  • 2nd Retake: -{penalty_config['second_retake']} marks")
    print(f"  • Late Arrival: -{penalty_config['late_comer']} marks")

    print("\nSet Distribution:")
    for set_num, count in sorted(set_counts.items()):
        print(f"  • Set {set_num}: {count} students")

    print("\n" + "-"*110)
    print("DETAILED STUDENT ASSIGNMENT LIST")
    print("-"*110)
    print(f"{'Roll Number':<18} | {'Status':<8} | {'Set':<4} | {'Retakes':<7} | {'Late':<4} | {'Penalty':<8} | {'Details':<30}")
    print("-"*110)

    for roll_num in sorted(tracker.keys()):
        data = tracker[roll_num]
        status = "PRESENT" if data["present"] else "ABSENT"
        set_no = str(data["set_number"]) if data["set_number"] is not None else "--"
        retakes = data["retake_count"]
        late = "YES" if data["late_comer"] else "NO"
        penalty = f"-{data['marks_penalty']}" if data['marks_penalty'] > 0 else "--"

        # Build details string
        details_parts = []
        if data["retake_history"]:
            retake_details = "; ".join([
                f"R{r['retake_number']}: {r['old_set']}→{r['new_set']}"
                for r in data["retake_history"]
            ])
            details_parts.append(retake_details)
        if data["late_comer"]:
            details_parts.append("Late arrival")

        details = "; ".join(details_parts) if details_parts else "--"

        print(f"{roll_num:<18} | {status:<8} | {set_no:<4} | {retakes:<7} | {late:<4} | {penalty:<8} | {details:<30}")

    print("="*110)

    students_with_penalty = [(roll, data) for roll, data in tracker.items() 
                            if data["marks_penalty"] > 0]

    if students_with_penalty:
        print("\n" + "="*70)
        print(" STUDENTS WITH MARKS PENALTY")
        print("="*70)
        print(f"{'Roll Number':<18} | {'Retakes':<7} | {'Late':<4} | {'Penalty':<10} | {'Set':<10}")
        print("-"*70)

        for roll_num, data in sorted(students_with_penalty, key=lambda x: x[1]['marks_penalty'], reverse=True):
            late = "YES" if data["late_comer"] else "NO"
            print(f"{roll_num:<18} | {data['retake_count']:<7} | {late:<4} | -{data['marks_penalty']:<9} | {data['set_number']:<10}")

        print("="*70)

    # Late comers section
    late_comers = [(roll, data) for roll, data in tracker.items() if data["late_comer"]]

    if late_comers:
        print("\n" + "="*70)
        print(" LATE COMERS SUMMARY")
        print("="*70)
        print(f"{'Roll Number':<18} | {'Set':<4} | {'Also Retook':<11} | {'Total Penalty':<15}")
        print("-"*70)

        for roll_num, data in sorted(late_comers):
            also_retook = "YES" if data["retake_count"] > 0 else "NO"
            print(f"{roll_num:<18} | {data['set_number']:<4} | {also_retook:<11} | -{data['marks_penalty']:<14}")

        print("="*70)


# ============================================================================
# 9. MAIN EXECUTION FLOW
# ============================================================================

def main():
    """Main function with all improvements including late comers."""

    print("="*70)
    print(" EXAM SET DISTRIBUTION SYSTEM")
    print("="*70)

    # Step 1: Configure Roll Numbers
    all_roll_numbers = get_roll_numbers_simplified()

    # Step 2: Configure Penalties (Retake + Late Comer)
    penalty_config = get_penalty_config_from_user()

    # Step 3: Initialize Enhanced Tracker
    exam_tracker = initialize_exam_tracker_enhanced(all_roll_numbers)
    set_history = {"history": []}

    # Step 4: Select Distribution Mode
    print("\n" + "="*70)
    print(" DISTRIBUTION MODE SELECTION")
    print("="*70)

    while True:
        print("\nSelect distribution mode:")
        print("1: Teacher-led Sequential Order")
        print("2: Student-initiated Roll Number Entry")
        print("3: Fully Random Distribution")

        mode_choice = input("\nEnter your choice (1, 2, or 3): ").strip()

        if mode_choice == '1':
            distribute_by_sequence(all_roll_numbers, exam_tracker, set_history)
            break
        elif mode_choice == '2':
            distribute_by_roll_number(all_roll_numbers, exam_tracker, set_history)
            break
        elif mode_choice == '3':
            distribute_fully_random(all_roll_numbers, exam_tracker, set_history)
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Step 5: Handle Late Comers
    handle_late_comers(exam_tracker, set_history, penalty_config)

    # Step 6: Handle Retakes with Penalty
    handle_retakes_with_penalty(exam_tracker, set_history, penalty_config)

    # Step 7: Generate Enhanced Report
    generate_report_enhanced(exam_tracker, penalty_config)

    print("\n" + "="*70)
    print(" EXAM DISTRIBUTION COMPLETE")
    print("="*70)


if __name__ == "__main__":
    main()
