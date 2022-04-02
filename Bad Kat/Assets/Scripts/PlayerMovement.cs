using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public float turnSpeed = 20f;
    public float movementSpeed = 0.05f;
    public Transform cam;
    public float attackSpeed = 2f;

    List<Enemy> m_EnemiesInRange = new List<Enemy>();

    float m_HitAt;
    float m_AttackTimeRemain;
    bool m_IsAttacking;
    bool m_Attacked;

    Vector3 m_Movement;

    Animator m_Animator;
    CharacterController m_Controller;

    // Start is called before the first frame update
    void Start()
    {
        m_Animator = GetComponent<Animator>();
        m_Controller = GetComponent<CharacterController>();

        m_HitAt = 0.3f * attackSpeed;
        m_AttackTimeRemain = attackSpeed;
        m_IsAttacking = false;
        m_Attacked = true;

        Cursor.lockState = CursorLockMode.Locked;
    }

    // Update is called once per frame
    void Update()
    {
        float horizontal = Input.GetAxisRaw("Horizontal");
        float vertical = Input.GetAxisRaw("Vertical");

        m_Movement.Set(horizontal, 0f, vertical);
        m_Movement.Normalize();

        bool hasHorizontalInput = !Mathf.Approximately(horizontal, 0f);
        bool hasVerticalInput = !Mathf.Approximately(vertical, 0f);
        bool isWalking = hasHorizontalInput || hasVerticalInput;
        
        if (Input.GetMouseButtonDown(0) && !m_IsAttacking)
        {
            m_Animator.SetTrigger("Attack");
            m_AttackTimeRemain = attackSpeed;
            m_IsAttacking = true;
            m_Attacked = false;
        }

        if (m_AttackTimeRemain > 0f && m_IsAttacking)
        {
            isWalking = false;
            m_AttackTimeRemain -= Time.deltaTime;
        }

        if (m_AttackTimeRemain <= m_HitAt && !m_Attacked)
        {
            m_Attacked = true;
            HitInFront();
        }

        if (m_AttackTimeRemain <= 0f && m_IsAttacking)
        {
            m_AttackTimeRemain = attackSpeed;
            m_IsAttacking = false;
        }

        m_Animator.SetBool("IsWalking", isWalking);

        if (isWalking)
        {
            float targetAngle = Mathf.Atan2(m_Movement.x, m_Movement.z) * Mathf.Rad2Deg + cam.eulerAngles.y;
            float angle = Mathf.SmoothDampAngle(transform.eulerAngles.y, targetAngle, ref turnSpeed, 0.1f);
            transform.rotation = Quaternion.Euler(0f, angle, 0f);

            Vector3 moveDir = Quaternion.Euler(0f, targetAngle, 0f) * Vector3.forward;
            moveDir.Normalize();
            m_Controller.Move(moveDir * movementSpeed * Time.deltaTime);
        }
    }

    public void HitInFront()
    {
        foreach(Enemy e in m_EnemiesInRange)
        {
            Debug.Log("Enemy " + e.GetInstanceID() + " hit!");
        }
    }

    public void AddEnemyInRange(Enemy enemy)
    {
        m_EnemiesInRange.Add(enemy);
    }

    public void RemoveEnemyInRange(Enemy enemy)
    {
        m_EnemiesInRange.Remove(enemy);
    }
}
